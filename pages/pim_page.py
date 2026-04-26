from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class PIMPage(BasePage):

    # search input field on employee list page
    EMPLOYEE_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")

    # search button
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Add Employee button
    ADD_EMPLOYEE_BTN = (By.XPATH, "//a[normalize-space()='Add Employee']")

    # No Records Found message
    NO_RECORDS_MSG = (By.XPATH, "//span[text()='No Records Found']")

    def is_on_employee_list_page(self):
        return "viewEmployeeList" in self.get_current_url()

    def is_employee_list_header_visible(self):
        time.sleep(2)
        try:
            element = self.driver.find_element(
                By.XPATH, "//*[normalize-space()='Employee List']"
            )
            return element.is_displayed()
        except Exception:
            return False

    def search_employee(self, name):
        self.type_text(self.EMPLOYEE_SEARCH_INPUT, name)
        time.sleep(1)
        self.click(self.SEARCH_BUTTON)
        time.sleep(4)  # OrangeHRM search is slow - wait longer for results
        return self

    def get_result_rows(self):
        # try multiple locator strategies to find result rows
        # OrangeHRM sometimes renders the table differently
        try:
            time.sleep(2)

            # strategy 1: look for rows inside the table body
            rows = self.driver.find_elements(
                By.XPATH,
                "//div[@class='oxd-table-body']//div[@role='row']"
            )
            if len(rows) > 0:
                return rows

            # strategy 2: broader search - any row in results area
            rows = self.driver.find_elements(
                By.XPATH,
                "//div[contains(@class,'oxd-table-row')]"
            )
            # filter out header row - actual data rows have more children
            data_rows = [r for r in rows if len(r.find_elements(By.XPATH, ".//div")) > 3]
            return data_rows

        except Exception:
            return []

    def is_no_records_displayed(self):
        return self.is_displayed(self.NO_RECORDS_MSG)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BTN)
        return self