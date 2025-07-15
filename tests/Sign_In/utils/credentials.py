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
    {"value": "q.e@squaresigns.com"},
    {"value": "qe@squaresigns.com"},
    {"value": "qe+randomstuff@squaresigns.com"},
    {"value": "qe.test.2.3.4.5@squaresigns.com"},
    {"value": "qe-@squaresigns.com"},
    {"value": "test@qa.devserver.com"},
    {"value": "qe!#$%^&*-_={}`~{}|/?'a@squaresigns.com"}
]