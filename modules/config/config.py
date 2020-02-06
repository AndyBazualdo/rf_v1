# Configurable variables for API
CLIENT_ID = "df3efa45-97d2-4c7e-9e21-147ac6cb9882"
CLIENT_SECRET = "QR1ro[OrEz2/iP/9.5AN-/dy-yHo482q"  # type: str
REDIRECT_URI = "https://app.getpostman.com/oauth2/callback"
BASE = "graph.microsoft.com"
RESOURCE = "https://" + BASE
AUTHORITY_URL = "https://login.microsoftonline.com/"
API_VERSION = "v1.0"
TENANT = "558e9515-7454-4ae9-995f-706a9f76beda"
BASE_URL = RESOURCE + "/" + API_VERSION
ON_BEHALF_USER = False


# Configurable variables for UI
class Config():
    DRIVER_TYPE= "Remote"
    EXECUTABLE_PATH="C:/D/PyWorkspace/amazon/drivers/chromedriver.exe"
    # BASE_URL = "http://blazedemo.com/"
    BASE_URL = "http://www.office.com/"
    IMPLICIT_TIME = 30
    REMOTE_DRIVER = "c"
