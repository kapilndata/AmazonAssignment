from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverUtils:

    def wait_till_all_elements_present(self, driver, locator):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.presence_of_all_elements_located(locator))

    def wait_till_element_visible(self, driver, locator):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.visibility_of_element_located(locator))