import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.sign_in_page import SignInPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    yield d
    d.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture
def sign_in_page(driver):
    return SignInPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)
