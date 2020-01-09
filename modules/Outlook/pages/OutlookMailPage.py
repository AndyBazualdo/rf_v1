import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver.common.by import By
from pom.PageBase import PageBase
from config.config import Config
from Outlook.locators.OutlookMailLocators import OutlookMailLocators

class OutlookMailPage(PageBase):

    def __init__(self):
        PageBase.__init__(self)
        self._web = self.getDriver()

    def verifyTitle(self):
        return self.get_element_value(OutlookMailLocators.APP_TITLE)

    def clickNewMessage(self):
        self.click(OutlookMailLocators.NEW_MESSAGE_BUTTON)

    def setDestMail(self, destEmail):
        self.enter_text(OutlookMailLocators.TO_FIELD_NEW_MESSAGE, destEmail)

    def setSubject(self, subject):
        self.enter_text(OutlookMailLocators.SUBJECT_FIELD_NEW_MESSAGE, subject)

    def setBody(self, body):
        self.enter_text(OutlookMailLocators.BODY_FIELD_NEW_MESSAGE, body)

    def sendNewMail(self):
        self.click(OutlookMailLocators.SEND_NEW_MESSAGE_BUTTON)

    def checkEmailSend(self):
        self.click(OutlookMailLocators.SEND_BUTTON_MAIN_MENU)
        return self.get_element_attribute_value(OutlookMailLocators.SENT_ITEMS_LIST,"aria-label")

    def openInbox(self):
        self.click(OutlookMailLocators.INBOX_BUTTON_MAIN_MENU)

    def openReceivedEmail(self, subject):
        self.click((By.XPATH, "//div[ @role ='option' and contains(@aria-label, '" + subject + "')]"))

    def checkEmailReceived(self, subject):
        return self.get_element_attribute_value((By.XPATH, "//div[@role='heading' and contains(@title,'"
                                                 + subject + "')]"), "title")