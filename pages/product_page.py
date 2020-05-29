
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    PAGE_SLUG = '/?promo=newYear'

    def should_be_product_url(self):
        assert self.PAGE_SLUG in self.browser.current_url, "Product page url is wrong"

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BSKTBUTTON_ADD), "Basket add is not found"

    def should_be_click_add_good_in_busket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BSKTBUTTON_ADD)
        add_button.click()
            
    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_VAL).text

    def get_success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_busket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def get_function_on_product_page(self):
        self.get_product_title()
        self.get_product_price()
        self.get_success_message()
        self.get_busket_price()

    def should_be_same_title_and_message(self):
        assert self.get_product_title() in self.get_success_message(), "Title do not match"

    def should_be_same_price_and_basket(self):
        assert self.get_product_price() in self.get_busket_price(), "Price do not match"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not found"
    
    def should_be_busket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Busket message is not found"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_VAL), "Busket message is not found"    