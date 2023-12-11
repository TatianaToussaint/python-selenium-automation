from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Click on cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    sleep(6)


@then('Verify “Your cart is empty” message is shown')
def verify_message(context):
    text_message = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert 'Your cart is empty' in text_message, f'Expected message is displayed in {text_message}'


