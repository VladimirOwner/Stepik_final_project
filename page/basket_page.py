from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Text is not here"

    def should_be_not_basket_text(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TEXT), "Text is here "

