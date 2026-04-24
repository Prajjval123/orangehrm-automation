from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# this file handles the OrangeHRM login page
# URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#
# how I found the locators:
# opened the login page → right clicked username field → Inspect
# saw <input name="username"> so I used By.NAME, "username"
# same for password: <input name="password">
# login button: <button type="submit"> so I used XPATH to find button with type submit
# error message: appeared after wrong login → inspected it → found the class name

class LoginPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # --- Locators ---

    # found by inspecting the username input field - it has name="username"
    USERNAME_INPUT = (By.NAME, "username")

    # found by inspecting the password field - it has name="password"
    PASSWORD_INPUT = (By.NAME, "password")

    # login button has type="submit" - used xpath to find a button with that attribute
    LOGIN_BUTTON   = (By.XPATH, "//button[@type='submit']")

    # error alert that appears when login fails
    # inspected it after a failed login → found this class pattern
    ERROR_MESSAGE  = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

    # --- Actions ---

    def open(self):
        # open the OrangeHRM login page
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        # type username, type password, click login
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def is_error_displayed(self):
        # check if the error message is visible after failed login
        return self.is_displayed(self.ERROR_MESSAGE)

    def get_error_message(self):
        # return the actual error text shown on screen
        return self.get_text(self.ERROR_MESSAGE)
