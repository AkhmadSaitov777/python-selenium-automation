import os

from behave import given, when, then

EMAIL    = os.getenv("TARGET_EMAIL", "akhmadsaitov.0420@gmail.com")
PASSWORD = os.getenv("TARGET_PASSWORD", "886644Qwerty")


# ── Given ────────────────────────────────────────────────────────────────────

@given("logged out user opens target.com")
def open_target_logged_out(context):
    context.main_page.open()


@given("user opens target.com")
def open_target(context):
    context.main_page.open()


# ── When ─────────────────────────────────────────────────────────────────────

@when("user clicks Sign In in header")
def click_sign_in_header(context):
    context.header_page.click_sign_in()


@when("user clicks on Cart icon")
def click_cart_icon(context):
    context.header_page.click_cart()


@when("user clicks Sign In from right side navigation menu")
def click_sign_in_right_nav(context):
    context.sign_in_page.click_sign_in_from_side_nav()


@when("user clicks Sign In from side navigation")
def click_sign_in_side_nav(context):
    context.sign_in_page.click_sign_in_from_side_nav()


@when('user searches for "{query}"')
def search_for_product(context, query):
    context.main_page.search(query)


@when("user clicks on first product")
def click_first_product(context):
    context.product_page.click_first_product()


@when("user clicks Add to Cart button")
def click_add_to_cart(context):
    context.product_page.click_add_to_cart()


@when('user inputs email "{_email}"')
def input_email(context, _email):
    context.sign_in_page.input_email(EMAIL)


@when('user inputs password "{_password}"')
def input_password(context, _password):
    context.sign_in_page.input_password(PASSWORD)


@when("user clicks Sign In button")
def click_sign_in_button(context):
    context.sign_in_page.click_sign_in_button()


# ── Then ─────────────────────────────────────────────────────────────────────

@then("Sign In form is opened")
def verify_sign_in_form_opened(context):
    assert context.sign_in_page.is_sign_in_form_visible(), \
        "Sign In form is not visible"


@then("product is added to cart successfully")
def verify_product_added(context):
    assert context.cart_page.is_product_in_cart(), \
        "Cart success message not visible — product may not have been added"


@then('"Your cart is empty" message is shown')
def verify_empty_cart(context):
    assert context.cart_page.is_empty_cart_message_visible(), \
        '"Your cart is empty" message is not visible'


@then("user is logged in and Sign In form disappears")
def verify_user_logged_in(context):
    assert not context.sign_in_page.is_sign_in_form_visible(), \
        "Sign In form still visible — login may have failed"
