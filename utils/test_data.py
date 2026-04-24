# all test data in one place
# OrangeHRM demo site credentials are publicly available on their demo page

# valid admin credentials for the demo site
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"

# wrong credentials to test invalid login
INVALID_USERNAME = "wronguser"
INVALID_PASSWORD = "wrongpassword"

# error message shown when wrong credentials are used
# I found this by actually logging in with wrong credentials and reading the error
ERROR_INVALID_CREDENTIALS = "Invalid credentials"

# an employee name that exists in the demo system
# searching this should return results
EXISTING_EMPLOYEE_NAME = "Admin"

# a name that definitely does not exist in the system
# searching this should show "No Records Found"
NON_EXISTING_EMPLOYEE_NAME = "XYZABC999NOTREAL"
