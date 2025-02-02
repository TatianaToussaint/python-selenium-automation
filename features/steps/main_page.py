from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@when('Click Sing In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(*SIDE_MENU_SIGN_IN).click()


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    number = int(number)  # convert str to int
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'


@when('Click on Cart icon')
def click_cart(context):
    context.app.main_page.click_cart()


@then('Verify header is present')
def verify_header_preset(context):
    context.driver.find_element(*HEADER)


@then('Verify “Your cart is empty” message is shown')
def verify_message(context):
    context.app.cart_page.verify_cart_empty_txt()
