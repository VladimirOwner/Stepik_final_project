import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPageChcek
import time
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page= ProductPage (browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage (browser, link)
    product_page.open()
    product_page.add_basket()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    chcek_product_page=ProductPageChcek(browser,link)
    chcek_product_page.open()
    chcek_product_page.add_to_basket()
    chcek_product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    chcek_product_page = ProductPageChcek(browser, link)
    chcek_product_page.open()
    chcek_product_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    chcek_product_page = ProductPageChcek(browser, link)
    chcek_product_page.open()
    chcek_product_page.add_to_basket()
    chcek_product_page.should_not_be_success_message_disp()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link ="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=BasketPage (browser,link)
    page.open()
    page.button_basket()
    page.should_be_basket_text()

@pytest.mark.need_review
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        email= str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        chcek_product_page = ProductPageChcek(browser, link)
        chcek_product_page.open()
        chcek_product_page.should_not_be_success_message()


    def test_guest_can_add_product_to_basket(self,browser):
        link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_basket()


