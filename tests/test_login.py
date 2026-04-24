from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    INVALID_USERNAME, INVALID_PASSWORD,
    ERROR_INVALID_CREDENTIALS
)

# all login test cases for OrangeHRM
# testing valid login, invalid login, empty fields, and logout

class TestHRMLogin:

    def test_valid_login_goes_to_dashboard(self, driver):
        # what I am testing: valid admin credentials should redirect to the dashboard
        #
        # steps:
        # 1. open login page
        # 2. type valid username and password
        # 3. click Login
        # 4. check URL contains "dashboard"

        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)

        dashboard = DashboardPage(driver)

        assert dashboard.is_on_dashboard(), \
            "after valid login the page should go to dashboard but it did not"

    def test_dashboard_header_visible_after_login(self, driver):
        # what I am testing: after login the Dashboard heading should be visible
        # this is a secondary check - not just the URL but the actual page content

        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)

        dashboard = DashboardPage(driver)

        assert dashboard.is_dashboard_header_visible(), \
            "Dashboard heading should be visible after login but it was not"

    def test_wrong_credentials_shows_error(self, driver):
        # what I am testing: entering wrong username/password should show an error alert

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "an error message should appear when wrong credentials are entered"

    def test_wrong_credentials_error_text(self, driver):
        # what I am testing: the error message should say "Invalid credentials"
        # checking the exact text not just that an error appeared

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

        actual_error = login_page.get_error_message()

        assert ERROR_INVALID_CREDENTIALS in actual_error, \
            f"expected '{ERROR_INVALID_CREDENTIALS}' but got: '{actual_error}'"

    def test_empty_username_shows_error(self, driver):
        # what I am testing: leaving username empty should trigger a validation error

        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", VALID_PASSWORD)  # empty username

        assert login_page.is_error_displayed(), \
            "error should appear when username is left empty"

    def test_logout_goes_back_to_login_page(self, driver):
        # what I am testing: after logging in and then clicking logout
        # the app should redirect back to the login page

        # first login
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)

        # then logout
        dashboard = DashboardPage(driver)
        login_page = dashboard.logout()

        assert "login" in login_page.get_current_url(), \
            "after logout the URL should contain 'login' but it did not"
