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

driver.get('//www.amazon.com')

# search by CSS, ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# search by CSS, classes+ tag:
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')

# search by CSS attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")

# search by CSS, Logo
driver.find_element(By.CSS_SELECTOR, "[class='a-icon a-icon-logo']")

# search by CSS, Create account
driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']")

# search by CSS, Your name field
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")

# search by CSS, Mobile number or email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# search by CSS, Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# search by CSS, "i"
driver.find_element(By.CSS_SELECTOR, "[class*='a-box-inner.a-alert-container']")

# search by CSS, Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# search by CSS, Continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

# search by CSS, Conditions of Use
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")

# search by CSS, Create account
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")

# search by CSS, Sign in link
driver.find_element(By.CSS_SELECTOR, "[class='a-link-emphasis']")


