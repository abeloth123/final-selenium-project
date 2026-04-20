from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def should_be_correct_product_name(self, expected_name):
        actual_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert actual_name == expected_name, f"Expected '{expected_name}', but got '{actual_name}'"

    def should_be_correct_basket_price(self, expected_price):
        actual_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE).text
        assert actual_price == expected_price, f"Expected '{expected_price}', but got '{actual_price}'"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text