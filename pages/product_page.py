
from .base_page import BasePage
from .locators import ProductPageLocators

from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    PAGE_SLUG = '/?promo=newYear'

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_button_add_basket()
        self.should_be_price_good()
        self.should_be_chek_basket_after_add_good()

    def should_be_product_url(self):
        assert self.PAGE_SLUG in self.browser.current_url, "Product page url is wrong"

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BSKTBUTTON_ADD), "Basket add is not found"

    def should_be_price_good(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_VAL)
        
        assert self.browser.find_element(*ProductPageLocators.PRICE_VAL), "Price is not found"

    def should_be_click_add_good_and_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_VAL).text
        add_button = self.browser.find_element(*ProductPageLocators.BSKTBUTTON_ADD)
        add_button.click()
        answer = self.browser.switch_to.alert
        answer.send_keys(solve_quiz_and_get_code)
        assert    self
