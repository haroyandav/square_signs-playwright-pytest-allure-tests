from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
from config import valid_email_with_adminPermission , valid_password_for_account_adminPermission , valid_email_for_google_sign_in , valid_password_for_google_sign_in
from tests.Sign_In.utils.credentials import invalid_passwords , invalid_emails , valid_emails
import time
from pages.design_tool import DesignTool

class SignIn(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.design_tool = DesignTool(page)

        # My account
        self.my_account = page.locator('[class="userDropDown  "]')
        self.my_account_dropdown = page.locator('[class="userDropDown-content-list"] > li')
        self.sign_in_button = page.locator('[class="userDropDown-content-list"] > li').nth(0)

        # Sign in modal
        self.email_field = page.locator('[data-testid="input-sign-in-email"][name="email"]')
        self.password_field = page.locator('[data-testid="input-sign-in-email"][name="password"]')
        self.log_in_button = page.locator('button[type="submit"]').nth(1)
        self.error_messages_field_is_required = page.locator('[data-testid="error-undefined"]')
        self.x_button = page.locator('[class="popupClose"]')

        # My account after Login
        self.user_name_desktop = page.locator('[class="titleBox user"] [class="desktop"]')

        # Sign in Google and Fb
        self.sign_in_continue_with_google = page.locator("[class='content popup-content'] button[type='button']").nth(1)
        self.sign_in_continue_with_facebook = page.locator("[class='content popup-content'] button[type='button']").nth(0)
        # self.email_field_google = page.locator('input[id="identifierId"]')

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
        messages = []
        for i in range(count):
            messages.append(self.get_text(locators.nth(i)))
        return messages , count
    
    def fill_email_field_with_valid_value(self):
        self.fill(self.email_field , value=valid_email_with_adminPermission)
        print('EMAIL' , valid_email_with_adminPermission)

    def fill_passowrd_field_with_valid_value(self):
        self.fill(self.password_field , valid_password_for_account_adminPermission)
    
    def clear_email_field(self):
        self.clear(self.email_field)
    
    def clear_password_field(self):
        self.clear(self.password_field)
        
    def clear_and_fill(self, locator: Locator, value: str, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)
        locator.fill("")
        locator.fill(value)

    def multiple_invalid_passwords(self):
        locator = self.error_messages_field_is_required
        for case in invalid_passwords:
            self.clear_and_fill(self.password_field, case["value"])
            self.click(self.log_in_button)
            error_text = self.get_text(locator)
            assert error_text == case['expected_error']

    def multiple_invalid_emails(self):
        locator = self.error_messages_field_is_required
        for case in invalid_emails:
            self.clear_and_fill(self.email_field , case['value'])
            self.click(self.log_in_button)
            error_text = self.get_text(locator.nth(0))
            assert error_text == case['expected_error']
    
    def multiple_valid_emails(self):
        locator = self.error_messages_field_is_required
        for case in valid_emails:
            self.clear_and_fill(self.email_field , case['value'])
            self.click(self.log_in_button)
            count = locator.count()
            assert count == 1
    
    def close_sign_in_modal(self):
        self.click(self.x_button)

    def get_user_name_after_login(self):
        return self.get_text(self.user_name_desktop)
    
    def sign_in_with_google(self):
        self.click(self.sign_in_continue_with_google)
        with self.page.expect_popup() as popup_info:
            self.click(self.sign_in_continue_with_google)

        popup = popup_info.value
        email_input = popup.locator('input#identifierId')
        self.fill(email_input, valid_email_for_google_sign_in)
        popup.get_by_text("Next").click()
    
    def sign_in_with_facebook(self):
        self.click(self.sign_in_continue_with_facebook)
    
    def valid_sign_in(self):
        self.hover_over_my_account()
        self.open_sign_in_modal()
        self.fill_email_field_with_valid_value()
        self.fill_passowrd_field_with_valid_value()
        self.click_on_the_sign_in_button()