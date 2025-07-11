from playwright.sync_api import Page
from pages.base_page import BasePage , Locator
import time

class ShoppingCart(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Shopping cart page , blocks
        self.cart_blocks = page.locator('[data-testid="cardListContainer"]')
        # Review items block in the shopping cart page
        self.review_items_block = self.cart_blocks.nth(0)
        # Saved for later in the shopping cart page
        self.saved_for_later_block = self.cart_blocks.nth(1)
        # Remove buutons for review items block
        self.review_items_remove_button = self.review_items_block.locator('button[data-testid="remove-cartItem"]')
        # Remove buttons for saved for later block
        self.saved_for_later_remove_button = self.saved_for_later_block.locator('button[data-testid="remove-cartItem"]')
        # All remove buttons without spacefic block
        self.all_remove_buttons = page.locator('button[data-testid="remove-cartItem"]')
        # Yes button after
        self.yes_after_remove = page.locator('[data-testid="button-confirm-remove-cartItem"]')
        # Proceed to checkout
        self.proceed_to_checkout = page.locator('[data-testid="proceedToCheckout"]')

    def remove_all_items_for_given_block(self , block):
        # Count once before starting
        time.sleep(2)
        if block == 'review_items':
            initial_count = self.review_items_remove_button.count()
            for _ in range(initial_count):
                self.click(self.review_items_remove_button.nth(0))
                self.page.wait_for_timeout(200)
                self.click(self.yes_after_remove)
                self.page.wait_for_timeout(300)
        elif block == 'saved_for_later':
            initial_count = self.saved_for_later_remove_button.count()
            for _ in range(initial_count):
                self.click(self.saved_for_later_remove_button.nth(0))
                self.page.wait_for_timeout(200)
                self.click(self.yes_after_remove)
                self.page.wait_for_timeout(300)
        else:
            initial_count = self.all_remove_buttons.count()
            for _ in range(initial_count):
                self.click(self.all_remove_buttons.nth(0))
                self.page.wait_for_timeout(200)
                self.click(self.yes_after_remove)
                self.page.wait_for_timeout(300)
    
    def navigate_to_checkout_page(self):
        self.click(self.proceed_to_checkout)
        url = self.page.url
        assert url == 'https://staging.squaresigns.com/checkout/'