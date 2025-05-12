# tests/retractable_banners/pricing/test_base_price.py

from pages.retractable_banners import RetractableBanners
from tests.retractable_banners.utils.priceUtils import get_base_price

def test_base_price_matches_ui(page):
    banner = RetractableBanners(page)

    # Step 1: Load expected base price from backend fixture
    expected_price = get_base_price()

    # Step 2: Deselect the default roll-up stand to isolate base price
    banner.unselect_default_option()

    # Step 3: Verify that the displayed price matches the expected base price
    banner.assert_price_is(expected_price)
