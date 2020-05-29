
import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

  
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_products_offer_url()
    page.should_be_button_add_basket()
    page.should_be_price()
    page.should_be_click_add_good_in_busket()
    page.solve_quiz_and_get_code()
    page.get_function_on_product_page()
    page.should_be_success_message()
    page.should_be_busket_message()
    page.should_be_same_title_and_message()
    page.should_be_same_price_and_basket()
    page.should_be_participate_in_offer()