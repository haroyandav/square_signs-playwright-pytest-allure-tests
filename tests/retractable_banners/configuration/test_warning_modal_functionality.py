# tests/retractable_banners/configuration/test_warning_modal_functionality.py

from pages.retractable_banners import RetractableBanners

def test_rollup_matches_selected_size(page):
    banner = RetractableBanners(page)

    # Step 1: Get the current selected size and roll-up values
    size_text = banner.get_size_field_text()
    rollup_text = banner.get_roll_up_stand_text()

    # Step 2: Extract numeric parts to compare (ignore units and symbols)
    size_digits = ''.join(filter(str.isdigit, size_text))
    rollup_digits = ''.join(filter(str.isdigit, rollup_text))

    # Step 3: Assert roll-up text contains the selected size digits
    assert size_digits in rollup_digits, "Roll-up does not match selected size"

    # Step 4: Scroll down and open the size dropdown
    page.evaluate("window.scrollBy(0, 150)")
    banner.click_size_field()

    # Step 5: Select a new, unchecked size option
    new_size = banner.select_random_unchecked_size()
    new_size_digits = ''.join(filter(str.isdigit, new_size))

    # Step 6: Wait for and confirm the warning modal
    banner.element_displayed(banner.warning_modal_heading, 4000)
    banner.confirm_notice_modal()
    page.wait_for_timeout(1000)  
    # Step 7: Get the updated size and roll-up text
    updated_size_digits = ''.join(filter(str.isdigit, banner.get_size_field_text()))
    updated_rollup_digits = ''.join(filter(str.isdigit, banner.get_roll_up_stand_button_text()))

    # Step 8: Assert that the updated roll-up matches the newly selected size
    assert new_size_digits == updated_size_digits, (
        f"Expected updated size to be '{new_size_digits}', but got '{updated_size_digits}'"
    )
    assert new_size_digits in updated_rollup_digits, (
        f"Updated roll-up does not include selected size: {updated_rollup_digits}"
    )