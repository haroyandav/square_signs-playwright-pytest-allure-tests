# tests/retractable_banners/configuration/test_unit_swich.py

from pages.retractable_banners import RetractableBanners

def test_unit_switching_updates_text_and_dropdown(page):
    banner = RetractableBanners(page)

    # Step 1: Switch to feet and verify
    banner.select_feet()
    assert banner.is_feet_selected(), "Feet unit should be selected"
    assert "feet" in banner.get_size_field_text().lower(), "Size text should contain 'feet'"

    banner.click_size_field()
    page.wait_for_timeout(500)
    sizes_feet = banner.get_all_size_options()
    assert all("feet" in option.lower() for option in sizes_feet), "All size options should be in feet"

    # Step 2: Switch to inch and verify
    banner.select_inch()
    assert banner.is_inch_selected(), "Inch unit should be selected"
    assert "inch" in banner.get_size_field_text().lower(), "Size text should contain 'inch'"

    banner.click_size_field()
    page.wait_for_timeout(500)
    sizes_inch = banner.get_all_size_options()
    assert all("inch" in option.lower() for option in sizes_inch), "All size options should be in inches"
