import time
from pages.Sign_in import SignIn

def test_sign_pop_up_fields_validation_t11454(page):
    
    home_page = SignIn(page)

    # hover over my account 
    home_page.hover_over_my_account()

    len_of_my_account_list = home_page.assert_len_of_my_account_modal()
    assert len_of_my_account_list == 3