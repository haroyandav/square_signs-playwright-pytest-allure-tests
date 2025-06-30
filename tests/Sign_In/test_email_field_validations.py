import time
from pages.Sign_in import SignIn
from tests.Sign_In.utils.messages import error_message_for_username_password_when_missing

def test_sign_in_pop_up_email_field_validations_t11453(page):

    sign_in = SignIn(page)

    # hover over my account 
    sign_in.hover_over_my_account()
    len_of_my_account_list = sign_in.assert_len_of_my_account_modal()
    assert len_of_my_account_list == 3
    
    # open sign in modal
    sign_in.open_sign_in_modal()
    sign_in.multiple_invalid_emails()
    sign_in.multiple_valid_emails()
