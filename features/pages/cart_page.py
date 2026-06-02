from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def is_empty_cart_message_visible(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MSG)
