from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the initial Sign In')
def click_initial_sign_in(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    sign_in_button.click()


@when('Clicks on the final Sign In')
def click_final_sign_in(context):
    final_sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    final_sign_in_button.click()


@then('Verify Sign In form opened')
def verify_sign_in_url(context):
    assert 'create_session_signin' in context.driver.current_url
