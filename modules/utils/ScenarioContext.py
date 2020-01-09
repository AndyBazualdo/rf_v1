class ScenarioContext(object):

    __context = {}

    def __init__(self):
        self.__context = dict()

    def set_context(self, key, value):
        self.__context.update({key: value})

    def get_context(self, key):
        return self.__context.get(key)
