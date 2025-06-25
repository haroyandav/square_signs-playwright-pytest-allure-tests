from playwright.sync_api import Page
from pages.base_page import BasePage , Locator

class SignIn(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # My account
        self.my_account = page.locator('[class="userDropDown  "]')
        self.my_account_dropdown = page.locator('[class="userDropDown-content-list"] > li')
    
    def hover_over_my_account(self):
        self.hover(self.my_account)
    
    def assert_len_of_my_account_modal(self):
        return self.my_account_dropdown.count()