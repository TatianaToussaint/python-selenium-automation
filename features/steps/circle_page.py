from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')


@when('User view the main section')
def benefit_boxes(context):
    wait = WebDriverWait(context.driver, 10)
    benefit_boxes_elements = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc']")))


@then('Five benefit boxes are present')
def verify_benefit_boxes(context):
    wait = WebDriverWait(context.driver, 10)
    benefit_boxes_elements = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*='styles__BenefitCard-sc']")))
    assert len(benefit_boxes_elements) == 5, f'Expected 5 benefit boxes, but got {len(benefit_boxes_elements)}'

