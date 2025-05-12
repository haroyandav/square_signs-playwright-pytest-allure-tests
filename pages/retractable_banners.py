from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import re
import random
import time

class RetractableBanners(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Unit toggle buttons
        self.unit_inch = page.locator('[data-testid="measurement-inch"]')
        self.unit_feet = page.locator('[data-testid="measurement-feet"]')

        # Size & pricing elements
        self.size_field_text = page.locator('.sc-gdyfxU .css-1dimb5e-singleValue')
        self.size_field = page.locator('.sc-gdyfxU .sc-ktPOXr')
        self.size_field_values_text = page.locator('[role="listbox"] .sc-eulNPF')
        self.price_section = page.locator('[data-testid="priceSection"]')
        self.roll_up_stand_field = page.locator('.css-1dimb5e-singleValue').nth(2)

        # Dropdowns
        self.dropdown_input = page.locator('.icon-arrow-down').nth(4)
        self.selected_option = page.locator('[id^="react-select-4"] .css-1dimb5e-singleValue')

        # Modal
        self.warning_modal_heading = page.locator('.warningPopupHeading')
        self.warning_modal_confirm_button = page.get_by_role('button', name='Confirm')
        self.warning_modal_cancel_button = page.get_by_role('button', name='Cancel')

        # Tooltip section
        self.buy_more_save_more = page.locator('[data-test-id="buy_more_save_more_product"]')

    # Unit selection
    def select_inch(self):
        self.click(self.unit_inch)

    def select_feet(self):
        self.click(self.unit_feet)

    def is_inch_selected(self) -> bool:
        return self.is_radio_selected(self.unit_inch)

    def is_feet_selected(self) -> bool:
        return self.is_radio_selected(self.unit_feet)

    # Modal confirmation
    def confirm_notice_modal(self) :
        self.click(self.warning_modal_confirm_button)

    # Buy More Save More
    def click_buy_more_save_more(self):
        self.page.get_by_text("Quantity", exact=True).scroll_into_view_if_needed()
        self.click(self.buy_more_save_more)

    def hover_buy_more_tooltip(self):
        self.hover(self.buy_more_save_more)

    # Size field
    def click_size_field(self):
        self.click(self.size_field)

    def get_size_field_text(self) -> str:
        return self.get_text(self.size_field_text)

    def get_roll_up_stand_text(self) -> str:
        return self.get_text(self.roll_up_stand_field)

    def get_all_size_options(self) -> list[str]:
        return self.get_all_texts(self.size_field_values_text)

    # Dropdown actions
    def open_dropdown(self):
        self.page.evaluate("window.scrollBy(0, 350)")
        self.click(self.dropdown_input)

    # Wait for at least one visible dropdown option reliably
        options = self.page.locator('[role="option"]')
        expect(options.first).to_be_visible(timeout=10000)

    def select_dropdown_option_by_text(self, option_text: str):
        self.click(self.dropdown_input)
        self.page.get_by_text(option_text, exact=True).click()

    def get_selected_option_text(self) -> str:
        content = self.selected_option.text_content()
        return content.strip() if content else ''

    def unselect_default_option(self):
        self.open_dropdown()
        first_option = self.page.locator('[role="option"]').first
        first_option.click()

    # Price assertion
    def assert_price_is(self, expected_price: float):
        text = self.price_section.inner_text()
        match = re.search(r'\$?(\d+(\.\d{1,2})?)', text)
        if not match:
            raise AssertionError(f"No price found in price section text: {text}")
        ui_price = float(match.group(1))
        assert abs(ui_price - expected_price) < 0.01, f"Expected {expected_price}, got {ui_price}"

    # Random size selection
    def select_random_unchecked_size(self) -> str:
        current = self.get_size_field_text().strip().lower()
        option_locator = self.page.locator('[role="option"]')
        count = option_locator.count()

        alternative_options = [
            option_locator.nth(i)
            for i in range(count)
            if option_locator.nth(i).inner_text().strip().lower() != current
        ]

        if alternative_options:
            selected = random.choice(alternative_options)
            selected_text = selected.inner_text().strip()
            selected.click()
            return selected_text
        return current
