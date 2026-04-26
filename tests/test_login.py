from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    INVALID_USERNAME, INVALID_PASSWORD,
    ERROR_INVALID_CREDENTIALS
)


class TestHRMLogin:

    def test_valid_login_goes_to_dashboard(self, driver):
        # valid credentials should redirect to dashboard
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        assert dashboard.is_on_dashboard(), \
            "after valid login the page should go to dashboard but it did not"

    def test_dashboard_header_visible_after_login(self, driver):
        # Dashboard heading should be visible after login
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        assert dashboard.is_dashboard_header_visible(), \
            "Dashboard heading should be visible after login but it was not"

    def test_wrong_credentials_shows_error(self, driver):
        # wrong username/password should show an error alert
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        assert login_page.is_error_displayed(), \
            "an error message should appear when wrong credentials are entered"

    def test_wrong_credentials_error_text(self, driver):
        # error message should say "Invalid credentials"
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        actual_error = login_page.get_error_message()
        assert ERROR_INVALID_CREDENTIALS in actual_error, \
            f"expected '{ERROR_INVALID_CREDENTIALS}' but got: '{actual_error}'"

    def test_empty_username_stays_on_login_page(self, driver):
        # OrangeHRM does not show a popup error for empty username
        # instead it just stays on the login page without navigating away
        # so we verify that the URL still contains "login" after clicking submit
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", VALID_PASSWORD)

        # if login failed correctly, we should still be on the login page
        assert "login" in driver.current_url, \
            "with empty username, page should stay on login but it navigated away"

    def test_logout_goes_back_to_login_page(self, driver):
        # after login and logout, should redirect back to login page
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        login_page = dashboard.logout()
        assert "login" in login_page.get_current_url(), \
            "after logout the URL should contain 'login' but it did not"