import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class ScenarioContext(object):
    __context = {}

    def __init__(self):
        self.__context = dict()

    @staticmethod
    def get_instance():
        if ScenarioContext.__context is None:
            ScenarioContext()
        return ScenarioContext.__context

    @staticmethod
    def set_context(key, value):
        ScenarioContext.__context.update({key: value})
        return ScenarioContext.__context

    @staticmethod
    def get_context(key):
        return ScenarioContext.__context.get(key)
