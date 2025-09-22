# Project 11 - Testing

This project contains a base application and a comprehensive test suite managed with **pytest**.  
Each branch originally corresponded to a specific issue or bug in the application.  
The tests for these fixes are present in each `tests` folder and can be run using **pytest**.  
Pytest settings are available and customizable in the `pytest.ini` file.

---

## 🚀 Installation

### 1. Clone the repository
```powershell
git clone https://github.com/Emilie2393/Projet_11_Testing.git
```

### 2. Create a virtual environment  
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```  

### 3. Install dependencies  
```powershell
pip install -r requirements.txt
```  

## 🧪 Running Tests with Pytest  

Run all tests from the project root:  

```powershell
pytest
```  

- Each tests folder contains test cases related to the fixes implemented in its corresponding branch.  

- The final version is available in the QA branch.  

## 🐝 Load Testing with Locust  
Locust simulates virtual users to test and measure the performance of your Flask application under real-world load conditions.  

To use it, proceed like following instructions:  

Run the Flask application with powershell:  

```powershell
$env:FLASK_APP="server:create_app"  
flask run  
```  

You can now access to the app into your browser: http://127.0.0.1:5000/  

Open another terminal:  

```powershell
locust -f tests/performance_tests/locustfile.py  
```  

You can now access to the Locust board in your browser: http://localhost:8089/  
Enter the simulate data of your choice and run Locust with the Flask app url: http://127.0.0.1:5000/  
