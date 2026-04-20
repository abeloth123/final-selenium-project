from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in message.lower(), "Empty basket message is not present"