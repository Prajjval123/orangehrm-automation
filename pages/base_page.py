from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# same concept as saucedemo base_page
# common methods written once here so all page files can reuse them
# OrangeHRM loads a bit slow so I use 15 second wait throughout

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # wait up to 15 seconds for elements - OrangeHRM can be slow
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        # wait until element is clickable then click
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        # wait for field to appear, clear it, then type
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        # wait for element to be visible and return its text
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_displayed(self, locator):
        # return True if visible, False if not found or hidden
        # try/except so it returns False instead of crashing if element doesn't exist
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            return False

    def get_current_url(self):
        # return the current browser URL
        return self.driver.current_url

    def get_all_elements(self, locator):
        # find all elements matching a locator and return as a list
        # used for counting rows in tables
        return self.wait.until(EC.presence_of_all_elements_located(locator))
