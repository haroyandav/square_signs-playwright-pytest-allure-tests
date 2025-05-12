# tests/retractable_banners/pricing/test_total_price.py

from pages.retractable_banners import RetractableBanners
from tests.retractable_banners.utils.priceUtils import (get_base_price, get_roll_up_options, calculate_total,)

def test_total_price_updates_on_dropdown_selection(page):
    banner = RetractableBanners(page)

    # Step 1: Retrieve base price from backend fixture
    base_price = get_base_price()

    # Step 2: Deselect default roll-up stand and verify the base price is displayed
    banner.unselect_default_option()
    banner.assert_price_is(base_price)

    # Step 3: Select a new roll-up stand from dropdown
    first_option = get_roll_up_options()[0]
    banner.select_dropdown_option_by_text(first_option['name'])

    # Step 4: Calculate expected total price with new roll-up stand
    expected_total = calculate_total(base_price, quantity=1, stand_price=first_option['price'])

    # Step 5: Verify that the displayed total matches the expected total
    banner.assert_price_is(expected_total)
