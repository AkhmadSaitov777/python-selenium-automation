from behave import given, when, then


@given("Open target.com")
def open_target(context):
    context.main_page.open()


@when("Click on Cart icon")
def click_cart_icon(context):
    context.main_page.click_cart()


@then('Verify "Your cart is empty" message is shown')
def verify_empty_cart(context):
    assert context.cart_page.is_empty_cart_message_visible(), \
        '"Your cart is empty" message is not visible'
