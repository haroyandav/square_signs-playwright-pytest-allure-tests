invalid_passwords = [
    {"value": "Pass1", "expected_error": "Password Must Be a Minimum of 6 Characters"},
    {"value": "123456", "expected_error": "Password Must Contain a Letter"},
    {"value": "passwo", "expected_error": "Password Must Contain a Digit"}
]