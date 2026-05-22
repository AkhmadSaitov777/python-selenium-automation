from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class SignInPage(BasePage):
    SIGN_IN_NAV_LINK       = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    EMAIL_INPUT            = (By.ID, "username")
    ENTER_PASSWORD_OPTION  = (By.CSS_SELECTOR, "div[id='password'][role='button']")
    PASSWORD_INPUT         = (By.CSS_SELECTOR, "input[id='password']")
    SIGN_IN_BUTTON         = (By.CSS_SELECTOR, "button[type='submit']")

    def is_sign_in_form_visible(self) -> bool:
        return self.is_visible(self.EMAIL_INPUT)

    def click_sign_in_from_side_nav(self):
        self.click(self.SIGN_IN_NAV_LINK)

    def input_email(self, email: str):
        field = self.find(self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email + Keys.RETURN)

    def click_enter_password_option(self):
        self.click(self.ENTER_PASSWORD_OPTION)

    def input_password(self, password: str):
        self.click_enter_password_option()
        field = self.find(self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_sign_in_button(self):
        self.click(self.SIGN_IN_BUTTON)
