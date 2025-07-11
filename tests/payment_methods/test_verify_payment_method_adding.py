import time
import pytest
from pages.design_tool import DesignTool
from pages.Sign_in import SignIn
from pages.shopping_cart import ShoppingCart
from pages.checkout import Checkout
from tests.payment_methods.utils.api import get_cart_quantity

def test_payment_method_functionality_by_adding_credit_debit_card_t126(page):

    design_tool = DesignTool(page)
    sign_in = SignIn(page)
    shopping_cart = ShoppingCart(page)
    checkout = Checkout(page)

    sign_in.valid_sign_in()
    get_cart_item_count = get_cart_quantity()
    response_count_json = get_cart_item_count.json()
    design_tool.navigation_to_design_tool_from_home_page()
    design_tool.click_add_to_cart_then_go_to_cart()
    get_cart_item_count_after_add_to_cart = get_cart_quantity()
    response_json_after_adding = get_cart_item_count_after_add_to_cart.json()
    assert response_json_after_adding > response_count_json

    shopping_cart.navigate_to_checkout_page()
    checkout.fill_the_shipping_step_fields()
    time.sleep(10)