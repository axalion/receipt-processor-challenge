# Flask Receipt Processing API

This Flask application processes receipts and calculates points based on specific rules.

## Prerequisites
- Python 3.9.12
- [requirements.txt](https://github.com/axalion/receipt-processor-challenge/blob/master/requirements.txt)


## Installation

### Installing Python 3.9.12

#### Mac
1. **Download Python 3.9.12:**
   - Go to the [Python Releases for macOS](https://www.python.org/downloads/macos/) page
   - Download the Python 3.9.12 installer (`python-3.9.12-macosx10.9.pkg`)

2. **Install Python:**
   - Open the downloaded `.pkg` file and follow the instructions to install Python

3. **Verify Installation:**
   - Open Terminal and run:
     ```bash
     python3 --version
     ```
   - You should see `Python 3.9.12`

#### Windows
1. **Download Python 3.9.12:**
   - Go to the [Python Releases for Windows](https://www.python.org/downloads/windows/) page
   - Download the Python 3.9.12 installer (`python-3.9.12-amd64.exe` for 64-bit or `python-3.9.12.exe` for 32-bit)

2. **Install Python:**
   - Run the downloaded `.exe` file
   - Ensure you check the box that says "Add Python to PATH"
   - Follow the instructions to complete the installation

3. **Verify Installation:**
   - Open Command Prompt and run:
     ```bash
     python --version
     ```
   - You should see `Python 3.9.12`.

#### Linux
1. **Install Python 3.9.12:**
   - Open Terminal and run the following commands:
     ```bash
     sudo apt update
     sudo apt install software-properties-common
     sudo add-apt-repository ppa:deadsnakes/ppa
     sudo apt update
     sudo apt install python3.9
     ```

2. **Verify Installation:**
   - Run:
     ```bash
     python3.9 --version
     ```
   - You should see `Python 3.9.12`


## Installation

### Clone the Repository
Clone the project repository to your local machine. The `<repository_directory>` refers to the directory created when you clone the repository, which will have the same name as the repository (in this case, `receipt-processor-challenge`)

```bash
# Clone the repository from GitHub
git clone https://github.com/axalion/receipt-processor-challenge.git

# Navigate into the repository directory
cd receipt-processor-challenge
```

### Set Up Virtual Environment
It's a good practice to use a virtual environment to manage dependencies

### Max and Linux

1. **Create a virtual environment:**
```bash
python3 -m venv myapp
```

2. **Activate the virtual environment:**
```bash
source myapp/bin/activate
```


### Windows
1. **Create a virtual environment:**
```bash
python -m venv myapp
```

2. **Activate the virtual environment:**
```bash
source myapp/bin/activate
```

3. **If you encounter a policy error when trying to activate the virtual environment, you need to change the execution policy for PowerShell scripts:**
   - Open PowerShell as Administrator: Right-click on the Start menu, select "Windows PowerShell (Admin)" or "Windows Terminal (Admin)"
   - Check the current execution policy:
     ```bash
      Get-ExecutionPolicy
      ```
   - Set the execution policy to allow script execution:
       ```bash
      Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
      ```
   - Activate the virtual environment:
      ```bash
      myapp\Scripts\Activate
      ```





### Install Dependencies

Install the required dependencies using the [requirements.txt](https://github.com/axalion/receipt-processor-challenge/blob/master/requirements.txt) file

```bash
pip install -r requirements.txt
```


### Run the Flask Application

With all dependencies installed, run the Flask server

```bash
python app.py

```


