from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify search worked for {search_results}')
def verify_search(context, search_results):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert search_results in search_results_header, f'Expected text {search_results} not in {search_results_header}'


@then('Verify {expected_keyword} search result url')
def verify_search(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, f'Expected {expected_keyword} not in {context.driver.current_url}'


@when('Click on add to Cart button')
def click_add_to_card(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='addToCartButton']").click()


@then('Verify cart has 1 item')
def store_product_name(context):
    context.driver.find_element(By.CSS_SELECTOR, "h4[class*='StyledHeading']")

