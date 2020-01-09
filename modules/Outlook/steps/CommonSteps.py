import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from pom.PageBase import PageBase
from config.config import Config

class CommonSteps(PageBase):
    __url = Config.BASE_URL

    def __init__(self):
        PageBase.__init__(self)
        self._web = self.getDriver()

    def open(self):
        self._web.get(self.__url)
        self.maximize_window()

    def close(self):
        self.close_all()
