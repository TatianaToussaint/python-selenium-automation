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
CONTACT_HELP_RECALLS_BLOCK = (By.CSS_SELECTOR, )
BROWSE_ALL_HELP = (By.ID, 'divID1')


@given('Open Target Help page')
def open_circle(context):
    context.driver.get('https://help.target.com/help')


@then('Verify UI elements')
def verify_title_present(context):
    context.driver.find_element(*TITLE)

#I am stuck with TC. Need more time to found out the way how I can organaze steps and scenario

