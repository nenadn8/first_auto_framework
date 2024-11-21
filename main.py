from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

# The following section sets up Webdriver and implicit wait
options = FirefoxOptions()
options.binary_location = r"D:\Firefox\firefox.exe"
driver = webdriver.Firefox(options = options)
driver.implicitly_wait(5)  # seconds

# Set-up operations
home_page = "https://www.letskodeit.com/"
driver.maximize_window()
driver.get(home_page)

# Signing in | Using @id first for better (faster) performance below
sign_in_button = driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/login']")
sign_in_button.click()

email_field = driver.find_element(By.XPATH, "//div[@id='page']//input[@tabindex='4']") # page has two id='email' elements
email_field.send_keys("lijir81011@exoular.com")

password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys("t3st!!")

login_button = driver.find_element(By.ID, "login")
login_button.click()

# Checking if sign-in was successful
profile_icon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//img[@class='zl-navbar-rhs-img ']")
if profile_icon is not None:
    print("Login successful")
else:
    print("Login failed")

driver.close()
