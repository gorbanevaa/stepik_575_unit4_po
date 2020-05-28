from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BSKTBUTTON_ADD = (By.CSS_SELECTOR, '#add_to_basket_form')    
    BASKET_FORM = (By.CSS_SELECTOR, '#btn-cart')
    PRICE_VAL = (By.CSS_SELECTOR, '.product_page .price_color')