from playwright.sync_api import Page, Locator, expect
import time

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Click on an element after waiting for it to be visible
    def click(self, locator: Locator, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)
        locator.click()

    # Fill an input field after it becomes visible
    def fill(self, locator: Locator, value: str, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)
        locator.fill(value)

    # Get text content from an element after it becomes visible
    def get_text(self, locator: Locator, timeout: int = 10000) -> str:
        locator.wait_for(state="visible", timeout=timeout)
        return locator.text_content().strip()

    # Get all inner texts from matched elements
    def get_all_texts(self, locator: Locator) -> list[str]:
        return locator.all_inner_texts()

    # Hover over an element after it becomes visible
    def hover(self, locator: Locator, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)
        locator.hover()

    # Check if a radio button or checkbox is selected after visibility check
    def is_radio_selected(self, locator: Locator, timeout: int = 10000) -> bool:
        locator.wait_for(state="visible", timeout=timeout)
        return locator.is_checked()

    # Assert that the element is visible using Playwright's expect
    def element_displayed(self, element: Locator, timeout: int = 10000):
        expect(element).to_be_visible(timeout=timeout)

    def clear(self, locator: Locator, timeout: int = 10000):
        locator.wait_for(state="visible", timeout=timeout)
        locator.fill("")