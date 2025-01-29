# forcepoint_assignment
First Part
Python task - Rides allocation (no special libraries required)
run the code using the following command: python3 rides_allocation.py



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



