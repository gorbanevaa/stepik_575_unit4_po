from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
   
    PAGE_SLUG = '/login'
   
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.PAGE_SLUG in self.browser.current_url, "Login url is wrong"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not found"
