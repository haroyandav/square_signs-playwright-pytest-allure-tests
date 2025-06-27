import time
from pages.Sign_in import SignIn
from tests.Sign_In.utils.messages import error_message_for_username_password_when_missing

def test_sign_pop_up_fields_validation_t11454(page):
    
    home_page = SignIn(page)

    # hover over my account 
    home_page.hover_over_my_account()
    len_of_my_account_list = home_page.assert_len_of_my_account_modal()
    assert len_of_my_account_list == 3
    
    # open sign in modal
    home_page.open_sign_in_modal()
    home_page.click_on_the_sign_in_button()

    messages , count = home_page.field_is_required_error_message_for_username_password()
    assert all(m == error_message_for_username_password_when_missing for m in messages)
    assert count == 2

    home_page.fill_email_field_with_valid_value()
    messages_after_email_filling , count_after_email_filling = home_page.field_is_required_error_message_for_username_password()
    assert count_after_email_filling == 1

    home_page.clear_email_field()
    home_page.fill_passowrd_field_with_valid_value()
    home_page.click_on_the_sign_in_button()
    messages_after_empty_email , count_if_email_empty = home_page.field_is_required_error_message_for_username_password()
    assert count_if_email_empty == 1

    home_page.fill_email_field_with_valid_value()
    home_page.test_multiple_invalid_passwords()