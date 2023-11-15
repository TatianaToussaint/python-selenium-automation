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


