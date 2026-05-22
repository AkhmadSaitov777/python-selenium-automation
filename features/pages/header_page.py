from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    CART_ICON    = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def click_sign_in(self):
        self.click(self.SIGN_IN_LINK)

    def click_cart(self):
        self.click(self.CART_ICON)
