from flask import Flask, request, jsonify
import math
from datetime import datetime
import time,re
from dateutil import parser

app = Flask(__name__)

# Dictionary to store JSON data
data_store = {}

def calculate_points(data):
    points = 0
    
    # Rule 1: One point for every alphanumeric character in the retailer name
    points += sum(char.isalnum() for char in data["retailer"])
    
    # Rule 2: 50 points if the total is a round dollar amount with no cents
    total = float(data["total"])
    if total.is_integer():
        points += 50
    
    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25
    
    # Rule 4: 5 points for every two items on the receipt
    points += (len(data["items"]) // 2) * 5
    
    # Rule 5: Points based on item description length and price
    for item in data["items"]:
        description = item["shortDescription"].strip()
        if len(description) % 3 == 0:
            price = float(item["price"])
            points += math.ceil(price * 0.2)
    
    # Rule 6: 6 points if the day in the purchase date is odd
    purchase_date = datetime.strptime(data["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6
    
    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm
    purchase_time = datetime.strptime(data["purchaseTime"], "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10
    
    return points 



def validate_data(data):
    # Define the required fields
    required_fields = ["retailer", "total", "items", "purchaseDate", "purchaseTime"]

    # Check for missing or blank required fields
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}", False
        
        # Check if the field is blank or contains only whitespace (except 'items')
        if field in ["retailer", "total", "purchaseDate", "purchaseTime"]:
            if not data[field] or not data[field].strip():
                return f"{field} cannot be blank", False

    # Validate purchaseDate
    try:
        # Attempt to parse the date
        purchase_date = datetime.strptime(data["purchaseDate"], "%Y-%m-%d")
        
        # Normalize to YYYY-MM-DD format
        data["purchaseDate"] = purchase_date.strftime("%Y-%m-%d")
        
    except ValueError:
        return "Invalid purchase date format, use YYYY-MM-DD", False

    # Validate purchaseTime
    try:
        datetime.strptime(data["purchaseTime"], "%H:%M")
    except ValueError:
        return "Invalid purchase time format, should be HH:MM", False

    # Validate total
    total_pattern = re.compile(r'^\d+\.\d{2}$')
    if not total_pattern.match(data["total"]):
        return "Invalid total format, use a number with two decimal places", False
    
    # Convert total to float and check if it's non-negative
    try:
        total = float(data["total"])
        if total < 0:
            return "Total amount must be non-negative", False
    except ValueError:
        return "Invalid total amount", False

    # Validate items
    if not isinstance(data["items"], list) or len(data["items"]) == 0:
        return "Items should be a non-empty list", False

    for item in data["items"]:
        # Check for required fields in each item
        if "shortDescription" not in item or "price" not in item:
            return "Each item must have 'shortDescription' and 'price'", False
        
        # Validate shortDescription
        short_desc_pattern = re.compile(r'^[\w\s\-]+$')
        if not short_desc_pattern.match(item["shortDescription"].strip()):
            return "Item shortDescription contains invalid characters", False
        
        # Validate price
        price_pattern = re.compile(r'^\d+\.\d{2}$')
        if not price_pattern.match(item["price"]):
            return "Invalid item price format, use a number with two decimal places", False
        
        # Convert price to float and check if it's non-negative
        try:
            price = float(item["price"])
            if price < 0:
                return "Item price must be non-negative", False
        except ValueError:
            return "Invalid item price", False

    return "Valid", True




@app.route('/receipts/process', methods=['POST'])
def save_data():
    # Generate a unique key based on the current time in nanoseconds
    unique_id = str(time.time_ns())
    
    # Get the JSON payload from the request
    json_payload = request.json
    
    # Normalize retailer name: replace multiple spaces with a single space
    if "retailer" in json_payload:
        json_payload["retailer"] = re.sub(r'\s+', ' ', json_payload["retailer"]).strip()
    
    # Validate the data
    validation_message, is_valid = validate_data(json_payload)
    if not is_valid:
        return jsonify({'error': validation_message}), 400
    
    # Calculate points
    points = calculate_points(json_payload)
    json_payload['points'] = points

    # Save the JSON payload in the dictionary with the nanosecond timestamp as the key
    data_store[unique_id] = json_payload

    # Return the unique ID
    return jsonify({'id': unique_id}), 201



@app.route('/receipts/<string:id>/points', methods=['GET'])
def get_data(id):
    # Retrieve the JSON data corresponding to the given ID
    json_data = data_store.get(id)

    if json_data is None:
        # If the ID is not found, return a 404 error
        return jsonify({'error': 'ID not found'}), 404
    
    # Calculate the points
    points_data = {}
    points_data["points"] = json_data['points']
    
    # Return the JSON data with points
    return jsonify(points_data), 200

if __name__ == '__main__':
    app.run(debug=True)
