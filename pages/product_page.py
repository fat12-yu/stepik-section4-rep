#!/usr/bin/python

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_basket_button()
        self.should_be_message_about()
        self.should_be_coast_equal()

    def should_be_add_basket_button(self):
        add_basket_button = self.get_element_present(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        assert add_basket_button is not None, "Add basket buton not found"
        add_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_message_about(self):
        product_name = self.get_element_present(*ProductPageLocators.PRODUCT_NAME)
        assert product_name is not None, "Product name not present"
        product_name = product_name.text

        message = self.get_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING)
        assert message is not None, "Message adding is not present"
        message = message.text
        assert product_name in message, "No product name in the message"

    def should_be_coast_equal(self):
        basket_total = self.get_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL)
        assert basket_total is not None, "Message basket total not found"
        basket_total = basket_total.text

        product_price = self.get_element_present(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price is not None, "Product price not found"
        product_price = product_price.text

        assert product_price in basket_total, "No product price in the message"
