
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

def test_guest_should_see_product_page_(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.should_be_button_add_basket()
    page.should_be_price()
    page.should_be_click_add_good_in_busket()
    page.solve_quiz_and_get_code()
    page.get_function_on_product_page()
    page.should_be_success_message()
    page.should_be_busket_message()
    page.should_be_same_title_and_message()
    page.should_be_same_price_and_basket()
   