from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product_text}')
def search_product(context, product_text):
    context.driver.find_element(By.ID, 'search').send_keys(product_text)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)


@when('Click Sign In')
def account_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify header is present')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'