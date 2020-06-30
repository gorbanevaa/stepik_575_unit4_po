from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")

class ProductPageLocators():
    PRODUCT_LINK = "?promo=newYear"   
    PRODUCTS_LINKS = "?promo=offerN"
    BSKTBUTTON_ADD = (By.CSS_SELECTOR, '#add_to_basket_form')    
    PRICE_VAL = (By.CSS_SELECTOR, '.product_page .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div .alert-success .alertinner strong')
    PRODUCT_TITLE =  (By.CSS_SELECTOR, '#content_inner h1')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div .alert-info .alertinner strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".navbar-nav a .icon-signin")   
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items .row")    
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")