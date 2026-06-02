from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://www.target.com"
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def open(self):
        super().open(self.URL)

    def click_cart(self):
        self.click(self.CART_ICON)
