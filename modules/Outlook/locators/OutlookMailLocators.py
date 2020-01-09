from selenium.webdriver.common.by import By


class OutlookMailLocators():
    APP_TITLE = (By.CSS_SELECTOR, "a[id = 'O365_AppName'] span")
    NEW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "span[id='id__3']")
    TO_FIELD_NEW_MESSAGE = (By.XPATH, "//div[contains(text(), 'To')]//following::input[1]")
    SUBJECT_FIELD_NEW_MESSAGE = (By.CSS_SELECTOR, "#subjectLine0")
    BODY_FIELD_NEW_MESSAGE = (By.CSS_SELECTOR, "div[aria-label='Message body'] div")
    SEND_NEW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Send']")
    SEND_BUTTON_MAIN_MENU = (By.XPATH,  "//i[@data-icon-name = 'Send'][1]")
    SENT_ITEMS_LIST = (By.XPATH,  "//div[contains(text(), 'To')]//following::div[1]")
    INBOX_BUTTON_MAIN_MENU = (By.XPATH,  "//i[@data-icon-name = 'Inbox'][1]")