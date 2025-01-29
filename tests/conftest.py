import pytest
from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright

#default URL
URL = 'http://127.0.0.1:4000/'

@pytest.fixture(scope="function", autouse=True)
def setup():
    """
    Fixture to set up the Playwright browser and page for each test function.
    Navigates to the default URL and yields the page object.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        print(page.title())
        yield page
        browser.close()


@pytest.fixture
def intercept_response(setup):
    """
    Fixture to intercept the response of the default URL and extract the captcha response.
    """
    with setup.expect_response(URL) as response_info:
        setup.reload()
        response = response_info.value.body()
        html_content = response.decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')

        captcha_response =  soup.find('input', {'type': 'hidden', 'name': 'correct_answer'})['value'] # Extract the correct answer from the hidden input field in response HTML

        yield (setup, captcha_response)