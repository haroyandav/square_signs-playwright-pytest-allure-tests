import math
import re
from pathlib import Path
import json
from pages.retractable_banners import RetractableBanners
from tests.retractable_banners.utils.priceUtils import get_base_price, get_roll_up_options

def load_backend_discounts():
    """Load and return sorted list of backend discounts with count and percent"""
    path = Path("tests/retractable_banners/utils/getDetailsFixture.json")
    with open(path) as f:
        data = json.load(f)
    discounts = sorted(data["discount"], key=lambda d: d["count"])
    return [{"count": d["count"], "percent": d["percent"]} for d in discounts]

def test_total_price_discount_calculation(page):
    banner = RetractableBanners(page)

    # Step 1: Load backend discount structure
    backend_discounts = load_backend_discounts()

    # Step 2: Calculate unit price from backend (base + default stand)
    base_price = get_base_price()
    rollup_price = get_roll_up_options()[0]['price']
    unit_price = round(base_price + rollup_price, 2)

    # Step 3: Open the quantity discount section in the UI
    banner.click_buy_more_save_more()
    page.wait_for_timeout(2000)

    quantity_buttons = page.locator('[class="sc-lnPyOc eajBbM"] > button')
    ui_row_count = quantity_buttons.count()

    assert ui_row_count == len(backend_discounts), \
        f"UI rows ({ui_row_count}) do not match backend rows ({len(backend_discounts)})"

    # Step 4: Loop through backend discounts and validate against UI
    for i, backend_discount in enumerate(backend_discounts):
        button = quantity_buttons.nth(i)

        # Extract values from UI
        ui_quantity = int(button.locator("span").first.inner_text().split()[0])
        ui_discount = int(button.locator("span").nth(3).inner_text().replace("% off", "").strip())

        # UI total value
        ui_total_text = button.locator("span").nth(2).inner_text()
        match = re.search(r'\d+(\.\d{1,2})?', ui_total_text)
        ui_total = float(match.group()) if match else None

        # Backend expected values
        backend_quantity = backend_discount["count"]
        backend_percent = backend_discount["percent"]

        # Validate quantity and discount %
        assert ui_quantity == backend_quantity, \
            f"Row {i+1}: Quantity mismatch. UI: {ui_quantity}, Backend: {backend_quantity}"

        assert ui_discount == backend_percent, \
            f"Row {i+1}: Discount mismatch. UI: {ui_discount}%, Backend: {backend_percent}%"

        # Calculate expected total price
        discounted_unit = round(unit_price * (1 - backend_percent / 100), 2)
        expected_total = round(discounted_unit * backend_quantity, 2)

        assert math.isclose(expected_total, ui_total, abs_tol=0.1), \
            f"Row {i+1}: Total mismatch. Expected: {expected_total}, UI: {ui_total}"