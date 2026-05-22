from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    SUCCESS_MODAL   = (By.XPATH, "//span[text()='Added to cart']")
    EMPTY_CART_MSG  = (By.XPATH, "//h1[text()='Your cart is empty']")

    def is_product_in_cart(self) -> bool:
        return self.is_visible(self.SUCCESS_MODAL)

    def is_empty_cart_message_visible(self) -> bool:
        return self.is_visible(self.EMPTY_CART_MSG)
