from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTest(unittest.TestCase):

    def test_login(self):
        # Webdriver and implicit wait setup
        options = FirefoxOptions()
        options.binary_location = r"D:\Firefox\firefox.exe"
        driver = webdriver.Firefox(options = options)
        driver.implicitly_wait(5)  # seconds

        # Set-up operations
        home_page = "https://www.letskodeit.com/"
        driver.maximize_window()
        driver.get(home_page)

        # Login
        login_page = LoginPage(driver)
        login_page.login("lijir81011@exoular.com", "t3st!!")

        # Asserts if sign-in was successful
        profile_icon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//img[@class='zl-navbar-rhs-img ']")
        if profile_icon is not None:
            print("Login successful")
        else:
            print("Login failed")

        driver.close()
