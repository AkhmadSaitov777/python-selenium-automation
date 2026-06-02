from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCou')]")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id='add']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
CART_COUNT = (By.CSS_SELECTOR, "[data-test='cartCount']")
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")
CART_PRODUCT_NAME = (By.CSS_SELECTOR, "h4.styles_ndsHeading__phw6r")
POPUP_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton']")
ADDED_TO_CART_CONFIRMATION = (By.CSS_SELECTOR, "span.h-text-lg")
VIEW_CART_BTN = (By.CSS_SELECTOR, "a[href='/cart']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com')
    sleep(3)


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(SEARCH_RESULTS_TEXT),
        message='Search results did not appear'
    )


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    btn = context.driver.find_element(*ADD_TO_CART_BTN)
    context.driver.execute_script("arguments[0].click();", btn)

    popup_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(POPUP_ADD_TO_CART_BTN)
    )
    popup_btn.click()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(ADDED_TO_CART_CONFIRMATION)
    )

@when('Store product name')
def store_product_name(context):
    context.product_before_adding = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text

@when('Open cart page')
def open_cart(context):
    view_cart_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(VIEW_CART_BTN)
    )
    view_cart_btn.click()
    sleep(3)


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    items = context.driver.find_elements(*CART_ITEMS)
    assert len(items) == int(expected_count), f'Expected {expected_count} items, got {len(items)}'


@then('Verify product in cart is correct')
def verify_product_in_cart(context):
    cart_product_name = context.driver.find_element(*CART_PRODUCT_NAME).text
    assert context.product_before_adding == cart_product_name, \
        f'Expected {context.product_before_adding}, got {cart_product_name}'