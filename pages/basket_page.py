from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_element_not_present(
            *BasketPageLocators.PRODUCT_IN_BASKET), "Product is presented in basket, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), "Message of empty basket is not presented"
