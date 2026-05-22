from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/title']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
