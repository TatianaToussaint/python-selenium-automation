from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('User view the main section')
def benefit_boxes(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc']")
    sleep(6)


@then('Five benefit boxes are present')
def verify_benefit_boxes(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc']")

