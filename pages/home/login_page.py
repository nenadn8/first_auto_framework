from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locator variables; using @id first for better (faster) performance below
    _sign_in_button = "//div[@id='navbar-inverse-collapse']//a[@href='/login']"
    _email_field = "//div[@id='page']//input[@placeholder='Email Address']"
    _password_field = "login-password"
    _login_button = "login"

    # Locator methods
    def locate_login_link(self):
        return self.driver.find_element(By.XPATH, self._sign_in_button)

    def locate_email_field(self):
        return self.driver.find_element(By.XPATH, self._email_field)

    def locate_password_field(self):
        return self.driver.find_element(By.ID, self._password_field)

    def locate_login_button(self):
        return self.driver.find_element(By.ID, self._login_button)

    # Action methods
    def click_sign_in_button(self):
        self.locate_login_link().click()

    def enter_username(self, email):
        self.locate_email_field().send_keys(email)

    def enter_password(self, password):
        self.locate_password_field().send_keys(password)

    def click_login_button(self):
        self.locate_login_button().click()

    # Login method
    def login(self, email, password):
        self.click_sign_in_button()
        self.enter_username(email)
        self.enter_password(password)
        self.click_login_button()
