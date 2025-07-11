from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
import time

class Checkout(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Shipping step in checkout
        self.commercial = page.locator('[data-testid="commercialLocation"]')
        self.residential = page.locator('[data-testid="residentialLocation"]')
        self.first_name = page.locator('[data-testid="firstNameInput"]')
        self.last_name = page.locator('[data-testid="lastNameInput"]')
        self.email = page.locator('[data-testid="emailInput"]')
        self.company_name = page.locator('[data-testid="companyNameInput"]')
        self.phone_number = page.locator('input[name="phone"]')
        self.phone_extension = page.locator('[data-testid="addressExtensionInput"]')
        self.address_line_1 = page.locator('[data-testid="input-google-autoComplete-input"]')
        self.address_line_2 = page.locator('[data-testid="addressFieldLine2"]')
        self.country_dropdown = page.locator('data-testid="Country:"')
        self.select_united_states = page.get_by_role('option' , name='United States')
        self.select_canada = page.get_by_role('option' , name='Canada')
        self.city = page.locator('[data-testid="addressFieldCity"]')
        self.state_dropdown = page.locator('[data-testid="State:"]')
        self.zip_code = page.locator('[data-testid="addressFieldZipCode"]')
        self.save_address_book_checkbox = page.get_by_role("checkbox", name="Save to Address Book")
        self.save_address_button = page.locator('[data-testid="button-save-address"]')

    def fill_the_shipping_step_fields(self):
        self.fill(self.first_name , 'Davit')
        self.fill(self.last_name , 'Haroyan')
        self.fill(self.email , 'davit.haroyan@gatsoft.am')
        self.fill(self.company_name , 'Company')
        self.fill(self.phone_number , '312) 642-1160')
        self.fill(self.address_line_1 , '1680')
        self.click(self.page.get_by_text('Intercontinental Park'))
        self.page.wait_for_timeout(200)
        self.click(self.save_address_book_checkbox)
        self.click(self.save_address_button)