from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage:
    TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        for _ in range(3):
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
                self.driver.execute_script("arguments[0].click();", element)
                return
            except StaleElementReferenceException:
                continue

    def is_visible(self, locator) -> bool:
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def is_not_visible(self, locator) -> bool:
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
