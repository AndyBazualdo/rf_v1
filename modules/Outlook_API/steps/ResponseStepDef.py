import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utils.ScenarioContext import ScenarioContext
from core.Authentication import Authentication
from core.RequestManager import RequestManager
from utils.EndPointHelper import EndPointHelper


class ResponseStepDef:
    __scenarioContext = None
    __response = None
    __requestSpecification = None
    __endpointHelper = EndPointHelper

    def __init__(self):
        self.__scenarioContext = ScenarioContext.get_instance()

    def print_results(self):
        print "\nHeaders: \n\n\t" + str(self.__response.headers)
        print "\nStatus code: \n\n\t" + str(self.__response.status_code)
        print "\nResponse: \n\n\t" + str(self.__response.content)
        # print "\nJson: \n\t" + str(self.__response.json())

    def i_should_see_the_status_code_as(self, code):
        self.__response = self.__scenarioContext.get('Last_Response')
        if self.__response.status_code is not int(code):
            raise AssertionError("Error: the request failed with status code: "
                                 + str(self.__response.status_code)
                                 + " \n response: \n" + str(self.__response.content))
        else:
            self.print_results()

    def the_value_is_equal_to(self, value_name, value):
        self.__response = self.__scenarioContext.get('Last_Response')
        if self.__response.json()[value_name] != value:
            raise AssertionError("Error: the request failed with status code: "
                                 + str(self.__response.status_code)
                                 + " \n response: \n" + str(self.__response.content))
        else:
            self.print_results()

    def the_value_is_not_null(self, value_name):
        self.__response = self.__scenarioContext.get('Last_Response')
        if self.__response.json()[value_name] is None:
            raise AssertionError("Error: the request failed with status code: "
                                 + str(self.__response.status_code)
                                 + " \n response: \n" + str(self.__response.content))
        else:
            self.print_results()
