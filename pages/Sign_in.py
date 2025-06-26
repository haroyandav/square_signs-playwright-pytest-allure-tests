from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
from config import valid_email_with_adminPermission , valid_password_for_account_adminPermission

class SignIn(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # My account
        self.my_account = page.locator('[class="userDropDown  "]')
        self.my_account_dropdown = page.locator('[class="userDropDown-content-list"] > li')
        self.sign_in_button = page.locator('[class="userDropDown-content-list"] > li').nth(0)

        # Sign in modal
        self.email_field = page.locator('[data-testid="input-sign-in-email"][name="email"]')
        self.password_field = page.locator('[data-testid="input-sign-in-email"][name="password"]')
        self.log_in_button = page.locator('button[type="submit"]').nth(1)
        self.error_messages_field_is_required = page.locator('[data-testid="error-undefined"]')
    
    def hover_over_my_account(self):
        self.hover(self.my_account)
    
    def assert_len_of_my_account_modal(self):
        return self.my_account_dropdown.count()
    
    def open_sign_in_modal(self):
        self.click(self.sign_in_button)

    def click_on_the_sign_in_button(self):
        self.click(self.log_in_button)
    
    def field_is_required_error_message_for_username_password(self):
        locators = self.error_messages_field_is_required
        count = locators.count()
        assert count == 2
        messages = []
        for i in range(count):
            messages.append(self.get_text(locators.nth(i)))
        return messages
    
    def fill_email_field_with_valid_value(self):
        self.fill(self.email_field , value=valid_email_with_adminPermission)