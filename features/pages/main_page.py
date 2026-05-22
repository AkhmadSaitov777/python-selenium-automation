from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://www.target.com"

    SEARCH_INPUT = (By.ID, "search")

    def open(self):
        super().open(self.URL)

    def search(self, query: str):
        search_box = self.find(self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(query + Keys.RETURN)
