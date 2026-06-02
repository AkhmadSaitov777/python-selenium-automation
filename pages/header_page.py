from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def click_sign_in(self):
        self.click(self.SIGN_IN_LINK)
