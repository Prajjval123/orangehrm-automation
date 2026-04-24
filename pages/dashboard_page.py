from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# this file handles the OrangeHRM dashboard
# after successful login you land here
# URL contains: /dashboard/index
#
# from the dashboard I can navigate to other modules like PIM (employee management)
# I can also logout from here using the dropdown at top right

class DashboardPage(BasePage):

    # --- Locators ---

    # the "Dashboard" heading visible after login
    # found by inspecting the heading text on the dashboard page
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    # the PIM link in the left sidebar - clicking it opens employee list
    # PIM stands for Personnel Information Management
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")

    # the user profile icon at top right - click to open dropdown
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")

    # the Logout option inside the dropdown menu
    LOGOUT_OPTION = (By.XPATH, "//a[text()='Logout']")

    # --- Actions ---

    def is_on_dashboard(self):
        # check if URL contains "dashboard" to confirm successful login
        return "dashboard" in self.get_current_url()

    def is_dashboard_header_visible(self):
        # check if the Dashboard heading is visible on screen
        return self.is_displayed(self.DASHBOARD_HEADER)

    def go_to_pim(self):
        # click PIM in the sidebar to go to the employee list
        self.click(self.PIM_MENU)
        from pages.pim_page import PIMPage
        return PIMPage(self.driver)

    def logout(self):
        # click the user icon at top right to open dropdown
        # then click Logout
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
