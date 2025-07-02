import time
import pytest
from pages.Sign_in import SignIn
from tests.Sign_In.utils.messages import error_message_for_username_password_when_missing

@pytest.mark.smoke
@pytest.mark.regression
def test_sign_in_validation_t11263(page , prepare_sign_in):
    # Given from fixture which doing Sign in backed request
    response_sign_in = prepare_sign_in
    response_sign_in_json = response_sign_in.json()
    user_full_name = f"{response_sign_in_json['firstName']} {response_sign_in_json['lastName']}"

    sign_in = SignIn(page)

    # hover over my account
    sign_in.hover_over_my_account()
    len_of_my_account_list = sign_in.assert_len_of_my_account_modal()
    assert len_of_my_account_list == 3
    
    # open sign in modal
    sign_in.open_sign_in_modal()
    sign_in.fill_email_field_with_valid_value()
    sign_in.fill_passowrd_field_with_valid_value()
    sign_in.click_on_the_sign_in_button()
    user = sign_in.get_user_name_after_login()
    assert user == user_full_name