from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product_text}')
def search_product(context, product_text):
    search_input_element = context.driver.find_element(By.ID, 'search')
    search_input_element.send_keys(product_text)
    search_button_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    search_button_element.click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")))


@when('Click Sign In')
def account_sign_in(context):
    account_link_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    account_link_element.click()
    sign_in_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    sign_in_element.click()
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")))


@then('Verify header is present')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(number), f'Expected {number} links, but got {len(links)}'