# tests/retractable_banners/ui/test_tab_navigation.py

import json
import pytest
from pathlib import Path
from playwright.sync_api import expect

# Load tab and heading test data from JSON fixture
def load_tab_data():
    data_file = Path("tests/retractable_banners/test_data/tab_navigation_data.json")
    with data_file.open() as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_tab_data())
def test_tab_navigation_displays_correct_heading(page, data):
    tab_label = data["tab"]
    expected_heading = data["heading"]

    # Step 1: Click the tab by matching its visible label
    page.locator(".product-tabs-slider-item-content").filter(has_text=tab_label).click()

    # Step 2: Verify that the expected heading is visible after clicking the tab
    heading = page.get_by_role("heading", name=expected_heading, exact=True)
    expect(heading).to_be_visible(timeout=5000)

