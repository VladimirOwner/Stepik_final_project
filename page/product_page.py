from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_basket(self):
        self.add_to_basket()
       # self.solve_quiz_and_get_code()
        self.should_be_name_book()
        self.should_be_price()


    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON), "Button is not presented"
    def should_be_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name_book_in_basket=self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        assert name_book.text ==  name_book_in_basket.text, "Book is wrong"
    def  should_be_price(self):
        price= self.browser.find_element(*ProductPageLocators.PRICE)
        price_in_basket=self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert  price.text == price_in_basket.text , "Price is wrong "

class ProductPageChcek(BasePage):
    def chcek(self):
        self.should_not_be_success_message()
        self.should_not_be_success_message_disp()
        self.add_to_basket()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_not_be_success_message_disp(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()




