import requests
from config import config

from core.Authentication import Authentication


class RequestManager:
    base = config.BASE_URL
    auth = Authentication.get_request_specification()

    @staticmethod
    def get(end_point, payload=None):
        url = RequestManager.base + end_point
        RequestManager.print_url(url)
        print payload
        response = requests.get(url=url, headers=RequestManager.auth, params=payload)
        print response.url
        return response

    @staticmethod
    def delete(end_point):
        url = RequestManager.base + end_point
        RequestManager.print_url(url)
        response = requests.delete(url=url, headers=RequestManager.auth)
        return response

    @staticmethod
    def put(end_point, payload=None):
        url = RequestManager.base + end_point
        RequestManager.print_url(url)
        response = requests.put(url=url, headers=RequestManager.auth, data=payload)
        return response

    @staticmethod
    def post(end_point, payload=None):
        url = RequestManager.base + end_point
        RequestManager.print_url(url)
        response = requests.post(url=url, headers=RequestManager.auth, data=payload)
        return response

    @staticmethod
    def patch(end_point, payload=None):
        url = RequestManager.base + end_point
        RequestManager.print_url(url)
        response = requests.patch(url=url, headers=RequestManager.auth, data=payload)
        return response

    @staticmethod
    def print_url(url):
        print "Endpoint used:  " + url
