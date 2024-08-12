### Tech Stack
1. Python 3.11
2. Requests - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest HTML
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute
### How to Install Packages
`pip install requests pytest pytest-html faker allure-pytest jsonschema` 

### To Freeze your Package version
`pip freeze > requirements.txt` 

## To Install te Freeze Version
`pip install -r requirements.txt` 

## How to run your Testcase Parallel
`pip install pytest-xdist` 

`pytest -n auto tests/integration_test/test_create_booking.py -s -v ` 

### To Work with the Excel
`pip install openpyxl` 

### To work wit JSON Schema
`pip install jsonschema` 

### How to run via Jenkins(CI/CD)
