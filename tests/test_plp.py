import time

from baseclass.baseclass import BaseClass
from pagefactory.homepage import HomePageFactory
from pagefactory.productlistingpage import ProductListingPage
from utils.generalutils import GeneralUtils


class TestHomepage(BaseClass):

    def test_search_product(self):
        plp_object = ProductListingPage(self.driver)
        search_product = GeneralUtils().get_product_test_data('search_product')
        no_of_search_results = GeneralUtils().get_product_test_data('no_of_products_on_plp')
        plp_object.land_on_plp(search_product)
        assert plp_object.validate_product_search(search_product) > no_of_search_results

    def test_apply_filter(self):
        plp_object = ProductListingPage(self.driver)
        general_utils = GeneralUtils()
        filter_min_price = general_utils.get_product_test_data('price_filter_min_value')
        filter_max_price = general_utils.get_product_test_data('price_filter_max_value')
        plp_object.apply_filter(filter_min_price, filter_max_price)
        assert plp_object.validate_price_filter(filter_min_price, filter_max_price), \
            "Filtered product price not in provided price filter range"






