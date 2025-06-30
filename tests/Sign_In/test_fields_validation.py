import time
from pages.Sign_in import SignIn
from tests.Sign_In.utils.messages import error_message_for_username_password_when_missing

def test_sign_in_pop_up_fields_validation_t11454(page):

    sign_in = SignIn(page)

    # hover over my account 
    sign_in.hover_over_my_account()
    len_of_my_account_list = sign_in.assert_len_of_my_account_modal()
    assert len_of_my_account_list == 3
    
    # open sign in modal
    sign_in.open_sign_in_modal()
    sign_in.click_on_the_sign_in_button()

    messages , count = sign_in.field_is_required_error_message_for_username_password()
    assert all(m == error_message_for_username_password_when_missing for m in messages)
    assert count == 2

    sign_in.fill_email_field_with_valid_value()
    messages_after_email_filling , count_after_email_filling = sign_in.field_is_required_error_message_for_username_password()
    assert count_after_email_filling == 1

    sign_in.clear_email_field()
    sign_in.fill_passowrd_field_with_valid_value()
    sign_in.click_on_the_sign_in_button()
    messages_after_empty_email , count_if_email_empty = sign_in.field_is_required_error_message_for_username_password()
    assert count_if_email_empty == 1

    sign_in.fill_email_field_with_valid_value()
    sign_in.multiple_invalid_passwords()