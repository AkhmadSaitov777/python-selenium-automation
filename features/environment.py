import os
import sys

# Add selenium_tests/ to path so 'pages' package is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.sign_in_page import SignInPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

    context.main_page = MainPage(context.driver)
    context.header_page = HeaderPage(context.driver)
    context.sign_in_page = SignInPage(context.driver)
    context.product_page = ProductPage(context.driver)
    context.cart_page = CartPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
