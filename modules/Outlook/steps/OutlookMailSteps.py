from Outlook.pages.OutlookMailPage import OutlookMailPage
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class OutlookMailSteps(object):
    __OutlookMailPage = None

    def __init__(self):
        self.__OutlookMailPage = OutlookMailPage()

    def app_title_is(self, title):
        res = self.__OutlookMailPage.verifyTitle()

        if res != title:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (title, res))

    def window_new_message_is_open(self):
        self.__OutlookMailPage.clickNewMessage()

    def set_destination_mail(self, destEmail):
        self.__OutlookMailPage.setDestMail(destEmail)

    def set_mail_subject(self, subject):
        self.__OutlookMailPage.setSubject(subject)

    def set_boby_content(self, body):
        self.__OutlookMailPage.setBody(body)

    def send_test_email(self):
        self.__OutlookMailPage.sendNewMail()

    def verify_email_was_sent(self, destEmail, subject):
        text = self.__OutlookMailPage.checkEmailSend()

        if destEmail not in text and subject not in text:
            raise AssertionError("Expected status to be email: '%s' and subject: '%s' were part of the last mail: '%s'"
                                 "sent." % (destEmail, subject, text))

    def open_inbox_section(self):
        self.__OutlookMailPage.openInbox()

    def open_received_email_with_subject(self, subject):
        self.__OutlookMailPage.openReceivedEmail(subject)

    def validate_received_email_can_be_opened(self, subject):
        text = self.__OutlookMailPage.checkEmailReceived(subject)

        if text != subject:
            raise AssertionError("Expected status to be email subject: '%s' is the same mail value: '%s'"
                                 " displayed in the title." % (subject, text))