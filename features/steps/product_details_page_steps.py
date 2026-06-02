from behave import given, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product blouse page')
def open_target(context):
    context.driver.get("https://www.target.com/p/women-s-smocked-blouse-universal-thread-red/-/A-95081560?preselect=95162150#lnk=sametab" )
    sleep(5)

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue', 'Brown', 'Red']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for c in colors:
        c.click()
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(SELECTED_COLOR)
        )

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]  # берём только название цвета
        selected_color = selected_color.split(' -')[0]  # убираем " - Out of Stock"
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'