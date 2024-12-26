from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTest(unittest.TestCase):

    # Set-up operations
    options = FirefoxOptions()
    options.binary_location = r"D:\Firefox\firefox.exe"
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)  # seconds
    home_page = "https://www.letskodeit.com/"
    login_page = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.home_page)
        self.login_page.login("lijir81011@exoular.com", "t3st!!")
        login_successful_result = self.login_page.login_successful()
        assert login_successful_result == True

        self.driver.close()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.home_page)
        self.login_page.login("lijir81011@exoular.com", "wrong_password")
        login_failed_result = self.login_page.login_failed()
        assert login_failed_result == True
