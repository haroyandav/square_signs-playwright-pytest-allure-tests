import time
import pytest
from pages.Sign_in import SignIn

@pytest.mark.smoke
@pytest.mark.regression
def test_sign_in_with_google_t11455(page):

    sign_in = SignIn(page)

    # hover over my account
    sign_in.hover_over_my_account()
    
    # open sign in modal
    sign_in.open_sign_in_modal()
    sign_in.sign_in_with_google()
    time.sleep(10)