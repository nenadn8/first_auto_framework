from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

# The following section sets up Webdriver and implicit wait.
options = FirefoxOptions()
options.binary_location = r"D:\Firefox\firefox.exe"
driver = webdriver.Firefox(options = options)
driver.implicitly_wait(5)    # seconds

# Basic operations and home page opening.
home_page = "https://www.letskodeit.com/"
driver.maximize_window()
driver.get(home_page)

# Signing in.
sign_in_button = driver.find_element(By.XPATH, "//a[@href='/login']")
sign_in_button.click()
