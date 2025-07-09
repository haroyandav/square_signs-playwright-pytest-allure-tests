import pytest
import requests
from tests.Sign_In.utils.api import get_header_cookie_for_valid_sign_in

def get_cart_quantity():
    endpoint = 'https://stagingapi.squaresigns.com/api/v1/Shopping/CartsQuantity'
    headers = get_header_cookie_for_valid_sign_in()
    response = requests.get(url=endpoint , headers=headers)
    return response