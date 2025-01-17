from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("one_time_setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.login_page = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login("lijir81011@exoular.com", "t3st!!")
        login_successful_result = self.login_page.login_successful()
        assert login_successful_result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login("lijir81011@exoular.com", "wrong_password")
        login_failed_result = self.login_page.login_failed()
        assert login_failed_result == True
