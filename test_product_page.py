
import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

  
# @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_products_offer_url()
#     page.should_be_button_add_basket()
#     page.should_be_price()
#     page.should_be_click_add_good_in_busket()
#     page.solve_quiz_and_get_code()
#     page.get_function_on_product_page()
#     page.should_be_success_message()
#     page.should_be_busket_message()
#     page.should_be_same_title_and_message()
#     page.should_be_same_price_and_basket()
#     page.should_be_participate_in_offer()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_good_in_busket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_good_in_busket()
    page.should_disappeared_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()    