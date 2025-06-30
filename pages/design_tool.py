from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
import time

class DesignTool(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        #Design tool button
        self.design_tool_button = page.locator('[data-unique-id="Design Tool Button"]')
    

    def navigation_to_design_tool_from_home_page(self):
        self.click(self.design_tool_button)