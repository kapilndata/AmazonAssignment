from selenium.webdriver.common.by import By
from pagefactory.homepage import HomePageFactory
from utils.generalutils import GeneralUtils
from utils.webdriverutils import WebDriverUtils


class ProductListingPage(GeneralUtils, WebDriverUtils):
    PLP_PRODUCT_LIST = None
    PLP_PRICE_FILTER_MIN_PRICE = (By.XPATH, "//div[@id='priceRefinements']//input[@placeholder='Min']")
    PLP_PRICE_FILTER_MAX_FILTER = (By.XPATH, "//div[@id='priceRefinements']//input[@placeholder='Max']")
    PLP_PRICE_FILTER_GO_BUTTON = (By.XPATH, "//div[@id='priceRefinements']//input[@type='submit']")
    PLP_PRODUCT_PRICE = (By.XPATH, "//div[contains(@data-component-type, 'search-result')]//span[contains(@class,'price-whole')]")

    def __init__(self, driver):
        self.driver = driver
        self.homepage = HomePageFactory(self.driver)

    def land_on_plp(self, product):
        self.homepage.search_product(product)

    def validate_product_search(self, product):
        product_name = product.capitalize()
        ProductListingPage.PLP_PRODUCT_LIST = (By.XPATH, f"//div[contains(@data-component-type, 'search-result')]//span[contains(text(),'{product_name}')]")
        self.wait_till_all_elements_present(self.driver, ProductListingPage.PLP_PRODUCT_LIST)
        no_of_products_on_plp = self.driver.find_elements(*ProductListingPage.PLP_PRODUCT_LIST)
        return len(no_of_products_on_plp)

    def apply_filter(self, min_price, max_price):
        self.wait_till_element_visible(self.driver, self.PLP_PRICE_FILTER_MIN_PRICE)
        min_price_input = self.driver.find_element(*self.PLP_PRICE_FILTER_MIN_PRICE)
        min_price_input.send_keys(min_price)
        max_price_input = self.driver.find_element(*self.PLP_PRICE_FILTER_MAX_FILTER)
        max_price_input.send_keys(max_price)
        price_filter_go_button = self.driver.find_element(*self.PLP_PRICE_FILTER_GO_BUTTON)
        price_filter_go_button.click()

    def validate_price_filter(self, min_price, max_price):
        product_prices = self.driver.find_elements(*self.PLP_PRODUCT_PRICE)
        product_price_list = self.remove_comma_from_product_price(product_prices)
        return_value = False
        for price in product_price_list:
            if max_price >= price >= min_price:
                return_value = True
        return return_value

