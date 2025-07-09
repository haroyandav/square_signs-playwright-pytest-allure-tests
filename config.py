from dotenv import load_dotenv
import os

load_dotenv()

valid_email_with_adminPermission = os.getenv("TEST_WEB_APP_EMAIL_ADMIN")
valid_password_for_account_adminPermission = os.getenv("TEST_WEB_APP_PASSWORD_ADMIN")
valid_email_for_google_sign_in = os.getenv("EMAIL_FOR_GOOGLE_SIGN_IN")
valid_password_for_google_sign_in = os.getenv("PASSWORD_FOR_GOOGLE_SIGN_IN")