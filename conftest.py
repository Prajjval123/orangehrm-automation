import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# same as saucedemo project - this opens and closes Chrome for every test automatically
# pytest reads this file on its own, I don't need to import it anywhere

@pytest.fixture
def driver():

    # open Chrome - webdriver manager handles the driver version automatically
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # maximize window so nothing is hidden or off screen
    driver.maximize_window()

    # wait up to 10 seconds for elements to load before failing
    # OrangeHRM is a heavier app than SauceDemo so it needs a bit more time
    driver.implicitly_wait(10)

    # yield = run the test now
    # before yield = setup, after yield = cleanup
    yield driver

    # close browser after test finishes
    driver.quit()
