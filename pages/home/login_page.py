from base.se_driver import SeDriver
import utilities.project_logger as project_logger
import logging

class LoginPage(SeDriver):

    log = project_logger.project_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator variables; using @id first for better (faster) performance below
    _sign_in_button = "//div[@id='navbar-inverse-collapse']//a[@href='/login']"
    _email_field = "//div[@id='page']//input[@placeholder='Email Address']"
    _password_field = "login-password"
    _login_button = "login"
    _login_fail_messages = ("//span[contains(text(), 'The email field is required.') or "
                            "contains(text(), 'The email must be a valid email address.') or "
                            "contains(text(), 'The password field is required.') or text()='Incorrect login details']")

    # Action methods
    def click_sign_in_button(self):
        self.click_on_element(self._sign_in_button, locator_type="xpath")
    def enter_username(self, email):
        self.enter_text(email, self._email_field, locator_type="xpath")
    def enter_password(self, password):
        self.enter_text(password, self._password_field)
    def click_login_button(self):
        self.click_on_element(self._login_button)

    def login(self, email="", password=""):
        self.click_sign_in_button()
        self.enter_username(email)
        self.enter_password(password)
        self.click_login_button()

    def login_successful(self):
        login_check = self.is_element_present("//button[@id='dropdownMenu1']//img[@class='zl-navbar-rhs-img ']",
                                         locator_type="xpath")
        return login_check

    def login_failed(self):
        self.wait_for_element(self._login_fail_messages, locator_type="xpath")
        login_fail_check = self.is_element_present(self._login_fail_messages, locator_type="xpath")
        return login_fail_check
