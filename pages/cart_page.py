from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    SUCCESS_MODAL = (By.XPATH, "//span[text()='Added to cart']")

    def is_product_in_cart(self) -> bool:
        return self.is_visible(self.SUCCESS_MODAL)
