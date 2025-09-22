# Project 11 - Testing

This project contains a base application and a comprehensive test suite managed with **pytest**.  
Each branch originally corresponded to a specific issue or bug in the application.  
The tests for these fixes are present in each `tests` folder and can be run using **pytest**.  
Pytest settings are available and customizable in the `pytest.ini` file.  

5 branches were made to bugfix some issues :  
- Point updates was not reflected on the main page, after they were on the booking page.  
- Entering a unknown email on the login page use to crashes the app.  
- Clubs were able to use more than their points allowed.  
- It was possible to book places for past competitions.  
- Clubs were able to book 12 places per competition. It's not allowed.  

1 branch is a new feature for the app :  
- We are now able to see the clubs points on the login page.  

QA branch is the merging of all those branches. The final app is created from this branch. Master branch is the original app.  

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

