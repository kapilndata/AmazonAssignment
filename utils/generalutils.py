import json
import os
from testdata.testdata import testdata


class GeneralUtils:

    def get_product_test_data(self, key):
        value = testdata['product_test_data'][key]
        return value

    def remove_comma_from_product_price(self, price_webelements_list):
        prices_list = [int(price.text.replace(',', '')) for price in price_webelements_list]
        return prices_list

