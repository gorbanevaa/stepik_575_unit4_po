
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    PAGE_SLUG = '/?promo=newYear'
    PAGE_SLUG_OFFER = '?promo=offer'

    def should_be_product_url(self):
        assert self.PAGE_SLUG in self.browser.current_url, "Product page url is wrong"

    def should_be_products_offer_url(self):
        assert self.PAGE_SLUG_OFFER in self.browser.current_url, "Offer product page url is wrong"    

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BSKTBUTTON_ADD), "Basket add is not found"

    def click_add_good_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BSKTBUTTON_ADD)
        add_button.click()
            
    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_VAL).text

    def get_success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def should_be_same_title_and_message(self):
        assert self.get_product_title() in self.get_success_message(), "Title do not match"

    def should_be_participate_in_offer(self):
        assert self.get_success_message() == "Coders at Work", "Link not participate in offer"   

    def should_be_same_price_and_basket(self):
        assert self.get_product_price() in self.get_basket_price(), "Price do not match"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"    

    def should_disappeared_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"                
    
    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "basket message is not found"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_VAL), "basket message is not found"    