import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from selenium import webdriver
from os import path
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from config.config import Config
from pyvirtualdisplay import Display

class WebDriverManager(object):

    __driver = None

    @classmethod
    def get_web_driver(cls):
        alreadyInstalled = False
        browser = Config.DRIVER_TYPE.lower()
        if cls.__driver is None:
            #display = Display(visible=0, size=(1366, 768))
            #display.start()
            if (path.exists(Config.EXECUTABLE_PATH)):
                alreadyInstalled = True
            if (browser.lower()) == "chrome":
                if (alreadyInstalled):
                    cls.__driver =  webdriver.Chrome(Config.EXECUTABLE_PATH)
                else:
                    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                    cls.__driver = driver

            if (browser.lower()) == "firefox":
                if (alreadyInstalled):
                    cls.__driver =  webdriver.Firefox(Config.EXECUTABLE_PATH)
                else:
                    cls.__driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

            if (browser.lower()) == "remote":
                if (Config.REMOTE_DRIVER == "c"):
                    chrome_options = Options()
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-dev-shm-usage')
                    cls.__driver =  webdriver.Remote(command_executor='http://localhost:4444/wd/hub', chrome_options=chrome_options, 
                    desired_capabilities=DesiredCapabilities.CHROME)
                if (Config.REMOTE_DRIVER == "f"):
                    cls.__driver =  webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)


            if (browser.lower()) == "chromeheadless":
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=1920x1080")
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--verbose")

                if (alreadyInstalled):
                    cls.__driver = webdriver.Chrome(Config.EXECUTABLE_PATH, chrome_options=chrome_options)
                else:
                    cls.__driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
                    cls.__driver.set_window_size(1920, 1080)

            #implicit wait webdriver
            cls.__driver.implicitly_wait(Config.IMPLICIT_TIME)

        return cls.__driver
