import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from pom.PageBase import PageBase
from config.config import Config
from project.locators.SearchFlightLocators import Locators

class SearchFlightPage(PageBase):
    __url = Config.BASE_URL

    def open(self):
        self._web.get(self.__url)

    def __init__(self):
        PageBase.__init__(self)
        self._web = self.getDriver()

    def select_departure_city(self, city):
        self.get_web_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(city)).click()

    def select_destination_city(self, city):
        self.get_web_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(city)).click()

    def search_for_flights(self):
        # self.get_web_element_by_xpath("//input[@type='submit']").click()
        self.click(Locators.SUBMIT_BUTTON)

    def get_found_flights(self):
        return self.get_web_elements_by_xpath("//table[@class='table']/tbody/tr")

    def close(self):
        self.close_all()
