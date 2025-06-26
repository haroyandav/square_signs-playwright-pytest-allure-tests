from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

valid_email_with_adminPermission = os.getenv("TEST_WEB_APP_EMAIL_ADMIN")
valid_password_for_account_adminPermission = os.getenv("TEST_WEB_APP_PASSWORD_ADMIN")