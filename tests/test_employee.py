import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    EXISTING_EMPLOYEE_NAME,
    NON_EXISTING_EMPLOYEE_NAME
)


class TestEmployeeManagement:

    @pytest.fixture(autouse=True)
    def login_and_go_to_pim(self, driver):
        # login and go to PIM module before every test
        LoginPage(driver).open().login(VALID_USERNAME, VALID_PASSWORD)
        dashboard = DashboardPage(driver)
        self.pim = dashboard.go_to_pim()

    def test_pim_opens_employee_list_page(self, driver):
        # clicking PIM should open employee list page
        assert self.pim.is_on_employee_list_page(), \
            "clicking PIM should go to employee list page but it did not"

    def test_employee_list_header_is_visible(self, driver):
        # Employee List heading should be visible
        assert self.pim.is_employee_list_header_visible(), \
            "Employee List heading should be visible but it was not"

    def test_search_existing_employee_returns_results(self, driver):
        # searching for a name that exists should return at least one result row
        self.pim.search_employee(EXISTING_EMPLOYEE_NAME)
        rows = self.pim.get_result_rows()

        # if still 0 rows, try once more with longer wait
        # OrangeHRM demo site can be slow sometimes
        if len(rows) == 0:
            import time
            time.sleep(3)
            rows = self.pim.get_result_rows()

        assert len(rows) > 0, \
            f"searching '{EXISTING_EMPLOYEE_NAME}' should return results but got 0 rows"

    def test_search_nonexistent_employee_shows_no_records(self, driver):
        # searching for a name that doesn't exist should show No Records Found
        self.pim.search_employee(NON_EXISTING_EMPLOYEE_NAME)
        assert self.pim.is_no_records_displayed(), \
            f"searching '{NON_EXISTING_EMPLOYEE_NAME}' should show No Records Found"

    def test_add_employee_button_navigates_correctly(self, driver):
        # clicking Add Employee should go to the add employee form
        self.pim.click_add_employee()
        assert "addEmployee" in driver.current_url, \
            "clicking Add Employee should open the add employee form but it did not"