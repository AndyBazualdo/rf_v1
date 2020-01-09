from Outlook.pages.LoginPage import LoginPage
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class LoginSteps(object):
    __loginPage = None

    def __init__(self):
        self.__loginPage = LoginPage()

    def access_to_sign_in_button(self):
        self.__loginPage.click_Sign_In_Button()

    def set_user_email_account(self, userMail):
        self.__loginPage.set_user_email(userMail)

    def set_user_password_account(self, userPass):
        self.__loginPage.set_user_password(userPass)

    def user_loged_is(self, userMail):
        self.__loginPage.validateLogin(userMail)

    def app_menu_is_visible(self):
        self.__loginPage.clickAppMenu()

    def outlook_app_is_opened(self):
        self.__loginPage.openOutlook()
