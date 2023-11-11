from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Click Orders
driver.find_element(By.ID, 'nav-orders').click()

# Find the heading on the Sign in page
sign_in = driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small' and contains(text(),'Sign in')]")

# Verify Sign in page opened
expected_result = 'Sign in'
actual_result = sign_in.text  # Get the text content of the element

assert expected_result == actual_result, f'Error. Expected text {expected_result} did not match actual text {actual_result}'
print('Test case passed!')

# verify email field present
driver.find_element(By.ID, 'ap_email')

sleep(5)
driver.quit()