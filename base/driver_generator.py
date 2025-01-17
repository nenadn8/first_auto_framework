from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class DriverGenerator():

    def __init__(self, use_browser):
        self.browser = use_browser

    def instantiate_webdriver(self):
        home_page = "https://www.letskodeit.com/"
        if self.browser == "firefox":
            options = FirefoxOptions()
            options.binary_location = r"D:\Firefox\firefox.exe"
            driver = webdriver.Firefox(options=options)
        elif self.browser == "edge":
            service = EdgeService(executable_path=r"C:\SeleniumDrivers\msedgedriver.exe")
            driver = webdriver.Edge(service=service)
        else: # for Chrome
            service = ChromeService(executable_path=r"C:\SeleniumDrivers\chromedriver.exe")
            driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.implicitly_wait(5)  # in seconds
        driver.get(home_page)
        return driver
