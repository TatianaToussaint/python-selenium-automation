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

# 1. Repeat everything I coded during the class.

driver.get('//www.amazon.com')

# search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')

# search by XPath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

# 2. Practice with locators. Homework.
# Create locators + search strategy

# search by XPath, "amazon logo"
driver.find_element(By.XPATH, "//input[@aria-label='Amazon']")

# search by ID, "Email field"
driver.find_element(By.ID, "ap_email")

# search by ID "Continue button"
driver.find_element(By.ID, "continue")

# search by ID "Conditions of use link"
driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[1]")

# search by ID "Privacy Notice link"
driver.find_element(By.ID, "legalTextRow")

# search by HPath "Need help link"
driver.find_element(By.XPATH, "//span[contains(@class='a-expander-prompt') and text()='Need help?']")

# search Forgot your password link
driver.find_element(By.ID,"auth-fpp-link-bottom")

# search Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# search by "Create your Amazon account button"
driver.find_element(By.ID, "createAccountSubmit")
