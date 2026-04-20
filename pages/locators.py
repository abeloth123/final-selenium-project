from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert:last-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child")