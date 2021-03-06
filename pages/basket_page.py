from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket empty "

    def check_no_items(self):    
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty!"