
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

def test_guest_should_see_product_page_(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
   