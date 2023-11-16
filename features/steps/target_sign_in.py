from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In')
def account_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_sign_in_url(context):
    assert 'create_session_signin' in context.driver.current_url
