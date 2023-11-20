from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TITLE = (By.CSS_SELECTOR,"[class='custom-h2']")
SEARCH_INPUT = (By.CSS_SELECTOR,"[class='search-input']")
TRACK_AN_ORDER = (By.CSS_SELECTOR, "[title='track an order']")
CURRENT_PROMO = (By.CSS_SELECTOR, "[title='view current promotions']")
PICKUP_DELIVERY = (By.CSS_SELECTOR, "[title='pickup & delivery']")
RETURNS = (By.CSS_SELECTOR, "[title='returns & receipts']")
GIFTCARD_BALANCE = (By.CSS_SELECTOR, "[title='check GiftCard balance']")
FIX_ISSUE = (By.CSS_SELECTOR, "[title='fix an issue']")
MANAGE_MY = (By.CSS_SELECTOR, "[class='manageMy']")
BROWSE_ALL_HELP = (By.ID, 'divID1')


@given('Open Target Help page')
def open_circle(context):
    context.driver.get('https://help.target.com/help')


@then('Verify UI elements')
def verify_ui_elements(context):
    title_element = context.driver.find_element(*TITLE)
    assert title_element.is_displayed()

    search_input_element = context.driver.find_element(*SEARCH_INPUT)
    assert search_input_element.is_displayed()

    track_an_order_element = context.driver.find_element(*TRACK_AN_ORDER)
    assert track_an_order_element.is_displayed()

    current_promo_element = context.driver.find_element(*CURRENT_PROMO)
    assert current_promo_element.is_displayed()

    pickup_delivery_element = context.driver.find_element(*PICKUP_DELIVERY)
    assert pickup_delivery_element.is_displayed()

    returns_element = context.driver.find_element(*RETURNS)
    assert returns_element.is_displayed()

    giftcard_balance_element = context.driver.find_element(*GIFTCARD_BALANCE)
    assert giftcard_balance_element.is_displayed()

    fix_issue_element = context.driver.find_element(*FIX_ISSUE)
    assert fix_issue_element.is_displayed()

    manage_my_element = context.driver.find_element(*MANAGE_MY)
    assert manage_my_element.is_displayed()

    browse_all_help_element = context.driver.find_element(*BROWSE_ALL_HELP)
    assert browse_all_help_element.is_displayed()

