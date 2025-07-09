from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
import time

class DesignTool(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        #Design tool button
        self.design_tool_button_home_page = page.locator('[data-unique-id="Design Tool Button"]')

        # Add to cart and Go to cart
        self.add_to_cart = page.locator('[class="designer-header-buttons-wrap"] button')
        self.go_to_cart = page.get_by_role("button", name="Go to Cart")

        # Guide design tool
        self.skip_button_guide = page.get_by_role("button", name="Skip")

    def navigation_to_design_tool_from_home_page(self):
        self.click(self.design_tool_button_home_page)

    def click_add_to_cart_then_go_to_cart(self):
        self.click(self.skip_button_guide)
        self.click(self.add_to_cart)
        self.click(self.go_to_cart)
        url = self.page.url
        assert url == 'https://staging.squaresigns.com/shopping-cart/'