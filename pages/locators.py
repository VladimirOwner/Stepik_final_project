from selenium.webdriver.common.by import By

class ProductPageLocators():
    BUTTON= (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK =  (By.CSS_SELECTOR, "[class=active]")
    PRICE = (By.CSS_SELECTOR , " div.col-sm-6:nth-child(2) .price_color")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR,"div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASS = (By.CSS_SELECTOR, 'input[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASS1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASS2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET= (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TEXT= (By.CSS_SELECTOR,"#content_inner p")