import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utils.ScenarioContext import ScenarioContext
from core.Authentication import Authentication
from core.RequestManager import RequestManager
from utils.EndPointHelper import EndPointHelper
import json
import time


class RequestStepDef:
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

    def user_authentication(self):
        self.__requestSpecification = Authentication.get_request_specification()
        if self.__requestSpecification['Authorization'] is None:
            raise AssertionError("Error: could not authenticate the account, "
                                 + "review the configuration set for connection")
        else:
            print self.__requestSpecification

    def send_get_request_to(self, end_point, account, params=None):
        self.__endpointHelper = EndPointHelper.build_endpoint(end_point, account)
        self.__response = RequestManager.get(self.__endpointHelper,params)
        self.__scenarioContext = ScenarioContext.set_context("Last_Response", self.__response)
        self.print_results()

    def send_get_request_with_wait_time(self, end_point, account, params=None):
        time.sleep(20)
        self.__endpointHelper = EndPointHelper.build_endpoint(end_point, account)
        self.__response = RequestManager.get(self.__endpointHelper,params)
        self.__scenarioContext = ScenarioContext.set_context("Last_Response", self.__response)
        self.print_results()

    def save_last_response_as(self, response_name):
        self.__scenarioContext = ScenarioContext.set_context(response_name, self.__response)

    def send_post_request_to(self, end_point, account, params):
        self.__endpointHelper = EndPointHelper.build_endpoint(end_point, account)
        self.__response = RequestManager.post(self.__endpointHelper, params)
        self.__scenarioContext = ScenarioContext.set_context("Last_Response", self.__response)
        print self.__scenarioContext.get("Last_Response").status_code
