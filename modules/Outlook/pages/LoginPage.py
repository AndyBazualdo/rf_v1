import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver.common.by import By
from pom.PageBase import PageBase
from config.config import Config
from Outlook.locators.LoginLocators import LoginLocators

class LoginPage(PageBase):

    def __init__(self):
        PageBase.__init__(self)
        self._web = self.getDriver()

    def click_Sign_In_Button(self):
        self.click(LoginLocators.SIGN_IN_BUTTON)

    def set_user_email(self,email):
        self.enter_text(LoginLocators.USER_MAIL, email)
        self.click(LoginLocators.LOGIN_BUTTON)

    def set_user_password(self,password):
        self.enter_text(LoginLocators.USER_PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)
        self.click(LoginLocators.EXTRA_BUTTON_LOGIN)

    def validateLogin(self, userMail):
        self.click(LoginLocators.PROFILE_BUTTON)
        self.get_element_value((By.CSS_SELECTOR,"[title='" + userMail + "']"))

    def clickAppMenu(self):
        self.click(LoginLocators.APP_MENU)

    def openOutlook(self):
        self.click(LoginLocators.OUTLOOK_BUTTON_APP_MENU)
