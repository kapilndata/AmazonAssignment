from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from baseclass.baseclass import BaseClass
from utils.webdriverutils import WebDriverUtils


class HomePageFactory(WebDriverUtils):

    HOMEPAGE_SEARCHBAR_LOCATOR = (By.XPATH, "//input[@id='twotabsearchtextbox']")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        self.wait_till_element_visible(self.driver, self.HOMEPAGE_SEARCHBAR_LOCATOR)
        search_bar = self.driver.find_element(*self.HOMEPAGE_SEARCHBAR_LOCATOR)
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.ENTER)

