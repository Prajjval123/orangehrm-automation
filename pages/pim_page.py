from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

# this file handles the PIM module (Employee List page)
# PIM = Personnel Information Management
# URL: /viewEmployeeList
#
# on this page you can:
# search for employees by name
# see a list of all employees
# click Add Employee to add a new one

class PIMPage(BasePage):

    # --- Locators ---

    # the search input field at the top of the employee list
    # it has a placeholder text "Type for hints..." - used that in the xpath
    EMPLOYEE_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")

    # the Search button below the filters
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # each row in the results table has this role
    # I count these rows to know how many results came back
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    # "Add Employee" button/link at the top of the page
    ADD_EMPLOYEE_BTN = (By.XPATH, "//a[normalize-space()='Add Employee']")

    # "Employee List" heading on the page
    EMPLOYEE_LIST_HEADER = (By.XPATH, "//h6[text()='Employee List']")

    # message shown when search returns zero results
    NO_RECORDS_MSG = (By.XPATH, "//span[text()='No Records Found']")

    # --- Actions ---

    def is_on_employee_list_page(self):
        # URL should contain "viewEmployeeList" when on this page
        return "viewEmployeeList" in self.get_current_url()

    def is_employee_list_header_visible(self):
        # check if the "Employee List" heading is visible
        return self.is_displayed(self.EMPLOYEE_LIST_HEADER)

    def search_employee(self, name):
        # type the employee name in the search box and click Search
        self.type_text(self.EMPLOYEE_SEARCH_INPUT, name)
        time.sleep(1)  # small wait for the autocomplete dropdown to settle
        self.click(self.SEARCH_BUTTON)
        time.sleep(2)  # wait for search results to load
        return self

    def get_result_rows(self):
        # find all rows in the results table and return as a list
        # if no rows found, return empty list instead of crashing
        try:
            rows = self.get_all_elements(self.TABLE_ROWS)
            return rows
        except Exception:
            return []

    def is_no_records_displayed(self):
        # check if "No Records Found" message is visible
        return self.is_displayed(self.NO_RECORDS_MSG)

    def click_add_employee(self):
        # click the Add Employee button
        self.click(self.ADD_EMPLOYEE_BTN)
        return self
