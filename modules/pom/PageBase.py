import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from wdm.WebDriverManager import WebDriverManager
from config.config import Config

class PageBase():
    """This class is the parent class for all the pages in our application."""
    driver = None
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self):
        self.driver = WebDriverManager.get_web_driver()
        self.wait = WebDriverWait(self.driver, Config.IMPLICIT_TIME)
        self.driver.set_script_timeout(50)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def get_web_element_by_xpath(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_web_elements_by_xpath(self, xpath):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def getDriver(self):
        return self.driver

    def close_all(self):
        return self.driver.quit()

    def maximize_window(self):
        return self.driver.maximize_window()

    def get_element_value(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def get_element_attribute_value(self, by_locator, attributeName):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute(attributeName)
