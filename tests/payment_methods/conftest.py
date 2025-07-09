# tests/conftest.py
import json
import time
import pytest
from playwright.sync_api import sync_playwright, Page, Browser
from ..payment_methods.utils.constants import BASE_URL

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page: Page = context.new_page()
        page.goto(BASE_URL)
        page.wait_for_timeout(1000)
        yield page
        browser.close()