# tests/conftest.py

import json
import time
import pytest
import requests
from requests.exceptions import RequestException
from playwright.sync_api import sync_playwright, Page, Browser
from .retractable_banners.utils.constants import BASE_URL, API_URL, FIXTURE_PATH

PRODUCT_PAYLOAD = {
    "id": 1112,
    "width": 33,
    "height": 81
}

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def fetch_api_data_with_retries(url, payload, max_retries=MAX_RETRIES, delay=RETRY_DELAY):
    """
    Send a POST request to the product API with retry logic and exponential backoff.
    This ensures stability in case of transient network or backend issues.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                return response.json()
        except RequestException:
            pass

        attempt += 1
        time.sleep(delay * (2 ** (attempt - 1)))  # exponential backoff

    raise RuntimeError(f"Failed to fetch data from {url} after {max_retries} attempts")


@pytest.fixture(scope="session", autouse=True)
def prepare_api_fixture_once():
    """
    Run once per session:
    - Fetch product details via backend API
    - Store the response in a local JSON file as a fixture
    """
    data = fetch_api_data_with_retries(API_URL, PRODUCT_PAYLOAD)

    FIXTURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FIXTURE_PATH, "w") as f:
        json.dump(data, f, indent=2)

    yield

    # Clean up fixture file after the test session
    with open(FIXTURE_PATH, "w") as f:
        f.write("{}")


@pytest.fixture(scope="function")
def page():
    """
    Create a fresh browser context before each test:
    - Launch Chromium in headless mode
    - Navigate to the product page
    - Close the browser after test execution
    """
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page: Page = context.new_page()
        page.goto(BASE_URL)
        page.wait_for_timeout(6000)
        yield page
        browser.close()
