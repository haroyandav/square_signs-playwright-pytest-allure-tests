invalid_passwords = [
    {"value": "Pass1", "expected_error": "Password Must Be a Minimum of 6 Characters"},
    {"value": "123456", "expected_error": "Password Must Contain a Letter"},
    {"value": "passwo", "expected_error": "Password Must Contain a Digit"}
]

invalid_emails =[
    {"value": "-qe@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe.@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe@test@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe test@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe(test)a@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe[test]a@squaresigns.com", "expected_error": "Wrong Email Address"}
]

valid_emails =[
    {"value": "q.e@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe+randomstuff@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe.test.2.3.4.5@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "qe-@squaresigns.com", "expected_error": "Wrong Email Address"},
    {"value": "test@qa.devserver.com", "expected_error": "Wrong Email Address"},
    {"value": "qe!#$%^&*-_={}`~{}|/?'a@squaresigns.com"}
]