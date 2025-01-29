# forcepoint_assignment
First Part
Python task - Rides allocation (no special libraries required)

Run the code using the following command: python3 rides_allocation.py
In order to change the input pls update requested_rides.csv in resources folder
The output file located in resources folder as well

    """
    Main cases to test:
    1. all rides approved - in external_service_mock.py return 'ride_request' instead approved_rides
    2. Not enough rides approved (less than 100)
    3. partial approval + fair distribution
    4. Optimal distribution (full fill chunk of 100 rides) - works with errors  
    """








Second Part
Playwright task - Web automation

Ensure you have the following installed on your system:
Python 3.10+
pip

Create a virtual environment (optional but recommended):
"python -m venv venv"

Install dependencies:
run requirements.txt using the following command: pip install -r requirements.txt

Install Playwright: for simplicity install only chromium browser for more information visit https://playwright.dev/python/docs/installation

playwright install chromium

**Important** before running the tests you should update URL in the confitest.py file , currently it is set to 'http://127.0.0.1:4000/' 

Run the tests
Run all : pytest -v (from the root directory)
Run happy flow: pytest -v -m positive (from the root directory)
Run negative flow: pytest -v -m negative (from the root directory)

***
Inorder to run the tests in headless mode pls update the following line in confitest.py file
    browser = playwright.chromium.launch(headless=False)
***
Inorder to generate html report please add --html-report=./report to the execution command -> *pytest -v --html-report=./report*

