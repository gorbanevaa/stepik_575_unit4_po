import time
import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" 
        email = str(time.time()) + "@fakemail.org"
        password = "q123456qwerty"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        
    
    def test_user_cant_see_success_message(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" 
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_basket()
        page.should_be_price()
        page.click_add_good_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_basket_message()
        page.should_be_same_title_and_message()
        page.should_be_same_price_and_basket()
        

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.click_add_good_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.click_add_good_to_basket()
    page.should_disappeared_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"     
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_add_basket()
    page.click_add_good_to_basket()
    page.should_be_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"     
    page = ProductPage(browser, link)
    page.open()   
    page.go_to_login_page()          
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_success_message(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()    

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"     
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_page = BasketPage(browser)
    basket_page.check_no_items()
    basket_page.empty_basket_message()    
