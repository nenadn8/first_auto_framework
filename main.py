from selenium import webdriver

driver = webdriver.Firefox("C:\SeleniumDrivers\geckodriver.exe")
driver.get("http://www.python.org")