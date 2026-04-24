import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    EXISTING_EMPLOYEE_NAME,
    NON_EXISTING_EMPLOYEE_NAME
)

# all employee management test cases
# testing the PIM module - employee list, search, and add employee

class TestEmployeeManagement:

    @pytest.fixture(autouse=True)
    def login_and_go_to_pim(self, driver):
        # runs automatically before every test in this class
        # logs in and navigates to the PIM / Employee List page
        # stores the pim page as self.pim so all tests can use it

        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        self.pim = dashboard.go_to_pim()

    def test_pim_opens_employee_list_page(self, driver):
        # what I am testing: clicking PIM in sidebar should open the employee list
        # I check the URL contains "viewEmployeeList"

        assert self.pim.is_on_employee_list_page(), \
            "clicking PIM should go to employee list page but it did not"

    def test_employee_list_header_is_visible(self, driver):
        # what I am testing: the "Employee List" heading should be visible on the page

        assert self.pim.is_employee_list_header_visible(), \
            "Employee List heading should be visible but it was not"

    def test_search_existing_employee_returns_results(self, driver):
        # what I am testing: searching for a name that exists should show at least one row
        # I use "Admin" as the search term because that employee exists in the demo system

        self.pim.search_employee(EXISTING_EMPLOYEE_NAME)

        rows = self.pim.get_result_rows()

        assert len(rows) > 0, \
            f"searching '{EXISTING_EMPLOYEE_NAME}' should return results but got 0 rows"

    def test_search_nonexistent_employee_shows_no_records(self, driver):
        # what I am testing: searching for a name that doesn't exist
        # should show "No Records Found" message

        self.pim.search_employee(NON_EXISTING_EMPLOYEE_NAME)

        assert self.pim.is_no_records_displayed(), \
            f"searching '{NON_EXISTING_EMPLOYEE_NAME}' should show No Records Found"

    def test_add_employee_button_navigates_correctly(self, driver):
        # what I am testing: clicking "Add Employee" should go to the add employee form
        # I verify this by checking the URL contains "addEmployee"

        self.pim.click_add_employee()

        assert "addEmployee" in driver.current_url, \
            "clicking Add Employee should open the add employee form but it did not"
