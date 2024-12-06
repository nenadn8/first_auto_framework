from selenium.webdriver.common.by import By
from traceback import print_stack

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeDriver():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        """Returns By.Type"""
        locator_type = locator_type.lower()
        locator_type_dictionary = {"id": By.ID, "name": By.NAME, "xpath": By.XPATH, "css": By.XPATH,
                                   "class_name": By.CSS_SELECTOR, "link_text": By.LINK_TEXT}
        if locator_type in locator_type_dictionary:
            return locator_type_dictionary[locator_type]
        else:
            print(f"Locator type {locator_type} not supported or input was incorrect."
                  "Accepted inputs are: id, name, xpath, css, class_name, link_text")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print(f"Element found using {locator_type}: {locator}")
        except:
            print(f"Element NOT found using {locator_type}: {locator}")
        return element

    def click_on_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print(f"Clicked on element using {locator_type}: {locator}")
        except:
            print_stack()
            print(f"Click on element failed using {locator_type}: {locator}")

    def enter_text(self, text, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(text)
            print(f"Sent text '{text}' to element using {locator_type}: {locator}")
        except:
            print_stack()
            print(f"Sending text '{text}' to element failed using {locator_type}: {locator}")

    def is_element_present(self, locator, locator_type="id"):
        try:
            presence_check = self.get_element(locator, locator_type)
            if presence_check is not None:
                print("Element present")
                return True
            else:
                print("Element NOT present")
                return False
        except:
            print("Element NOT present")
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            self.driver.implicitly_wait(0) # To not mix up implicit and explicit wait
            by_type = self.get_by_type(locator_type)
            print(f"Waiting for a maximum of {str(timeout)} seconds for the element to be visible.")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            wait.until(EC.presence_of_element_located((by_type, locator)))

            print("Element is visible on the page")
        except:
            print("Element is not visible on the page")
            print_stack()
        self.driver.implicitly_wait(5) # To not mix up implicit and explicit wait
        return element