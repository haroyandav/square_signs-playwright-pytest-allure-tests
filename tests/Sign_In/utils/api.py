import pytest
import requests
from config import valid_email_with_adminPermission , valid_password_for_account_adminPermission

def valid_sign_in():
    endpoint = 'https://stagingapi.squaresigns.com/api/v1/Account/SignIn'
    payload = {
    "username": valid_email_with_adminPermission,
    "password": valid_password_for_account_adminPermission
    }
    response = requests.post(url=endpoint , json=payload)
    return response