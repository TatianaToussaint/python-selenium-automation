from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_sign_in_url(context):
    assert 'create_session_signin' in context.driver.current_url
