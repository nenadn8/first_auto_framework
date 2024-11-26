from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Signing in | Using @id first for better (faster) performance below
        sign_in_button = self.driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/login']")
        sign_in_button.click()

        email_field = self.driver.find_element(By.XPATH, "//div[@id='page']//input[@placeholder='Email Address']")
        email_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "login-password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login")
        login_button.click()

