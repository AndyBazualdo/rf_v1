from selenium.webdriver.common.by import By

class LoginLocators():
    SIGN_IN_BUTTON = (By.XPATH, "//div[@id='meControl']")
    USER_MAIL = (By.XPATH, "//input[@name='loginfmt']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[id = 'idSIButton9']")
    USER_PASSWORD = (By.XPATH, "//input[@name='passwd']")
    EXTRA_BUTTON_LOGIN = (By.CSS_SELECTOR, "input[id = 'idBtn_Back']")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "[id = 'O365_MainLink_MePhoto']")
    APP_MENU = (By.CSS_SELECTOR, "[id='O365_MainLink_NavMenu']")
    OUTLOOK_BUTTON_APP_MENU = (By.CSS_SELECTOR, "[id='O365_AppTile_Mail']")