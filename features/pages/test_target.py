import os

from pytest_bdd import given, when, then, scenario, parsers

from pages.main_page import MainPage
from pages.header_page import HeaderPage
from pages.sign_in_page import SignInPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

EMAIL    = os.getenv("TARGET_EMAIL", "akhmadsaitov.0420@gmail.com")
PASSWORD = os.getenv("TARGET_PASSWORD", "123Qwerty.")


# ── Scenarios ────────────────────────────────────────────────────────────────

@scenario("../features/target.feature", "User opens sign in form from header")
def test_sign_in_form_opens():
    ...


@scenario("../features/target.feature", "User adds a product to cart")
def test_add_product_to_cart():
    ...


@scenario("../features/target.feature", "User logs in with valid credentials")
def test_user_login():
    ...


# ── Given ────────────────────────────────────────────────────────────────────

@given("logged out user opens target.com")
def open_target_logged_out(main_page):
    main_page.open()


@given("user opens target.com")
def open_target(main_page):
    main_page.open()


# ── When ─────────────────────────────────────────────────────────────────────

@when("user clicks Sign In in header")
def click_sign_in_header(header_page):
    header_page.click_sign_in()


@when("user clicks Sign In from right side navigation menu")
def click_sign_in_right_nav(sign_in_page):
    sign_in_page.click_sign_in_from_side_nav()


@when("user clicks Sign In from side navigation")
def click_sign_in_side_nav(sign_in_page):
    sign_in_page.click_sign_in_from_side_nav()


@when(parsers.parse('user searches for "{query}"'))
def search_for_product(main_page, query):
    main_page.search(query)


@when("user clicks on first product")
def click_first_product(product_page):
    product_page.click_first_product()


@when("user clicks Add to Cart button")
def click_add_to_cart(product_page):
    product_page.click_add_to_cart()


@when(parsers.parse('user inputs email "{email}"'))
def input_email(sign_in_page, email):
    sign_in_page.input_email(EMAIL)


@when(parsers.parse('user inputs password "{password}"'))
def input_password(sign_in_page, password):
    sign_in_page.input_password(PASSWORD)


@when("user clicks Sign In button")
def click_sign_in_button(sign_in_page):
    sign_in_page.click_sign_in_button()


# ── Then ─────────────────────────────────────────────────────────────────────

@then("Sign In form is opened")
def verify_sign_in_form_opened(sign_in_page):
    assert sign_in_page.is_sign_in_form_visible(), \
        "Sign In form is not visible"


@then("product is added to cart successfully")
def verify_product_added(cart_page):
    assert cart_page.is_product_in_cart(), \
        "Cart success message not visible — product may not have been added"


@then("user is logged in and Sign In form disappears")
def verify_user_logged_in(sign_in_page):
    assert not sign_in_page.is_sign_in_form_visible(), \
        "Sign In form still visible — login may have failed"

@then("user clicks Sign In button")
def click_sign_in_button(sign_in_page):
    sign_in_page.click_sign_in_button()
