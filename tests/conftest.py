import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", autouse=True)
def setup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:4000/')
        print(page.title())
        yield page
        browser.close()