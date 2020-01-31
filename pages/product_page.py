from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def should_message_right_information(self):
        self.should_message_name_of_adding_products()
        self.should_message_price_of_adding_products()

    def should_message_name_of_adding_products(self):
        origin_product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.get_element_text(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert origin_product_name == added_product_name, f"Name of product '{added_product_name}' in basket does not match with initial product '{origin_product_name}'"

    def should_message_price_of_adding_products(self):
        origin_product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.get_element_text(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert origin_product_price == added_product_price, f"Price of product '{added_product_price}'in basket does not match with price of initial product '{origin_product_price}'"

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_not_be_success_message(self):
        assert self.is_element_not_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"
