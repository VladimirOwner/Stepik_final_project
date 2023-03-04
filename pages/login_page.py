from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self,email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def should_be_register_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), "Pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), "Confirm pass field not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Register button not presented"


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login is not in this url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registr form is not presented"