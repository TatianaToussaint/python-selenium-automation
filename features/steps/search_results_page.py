from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
CART_SUMMARY = (By.CSS_SELECTOR, '.styles__CartSummarySpan-sc-odscpb-3.jaXVgU')

# CART_SUMMARY = (By.)

@then('Verify search worked for {search_results}')
def verify_search(context, search_results):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert search_results in search_results_header, f'Expected text {search_results} not in {search_results_header}'


@then('Verify {expected_keyword} search result url')
def verify_search(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, f'Expected {expected_keyword} not in {context.driver.current_url}'


@when('Click on add to Cart button')
def click_add_to_card(context):
    e = context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message="Element isn't clickable"
    )

    e.click()


@when('Open card page')
def open_cart(context):
    context.driver.get('https://target.com/cart')


@then('Verify cart has {amount} item(s)')
def verify_text(context, amount):
    text_content = context.driver.find_element(*CART_SUMMARY).text
    subtotal_index = text_content.index("subtotal")
    number_of_items = int(text_content[subtotal_index + len("subtotal"):].split()[0])