import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import adal
from config import config


class Authentication:
    header = None

    def __init__(self):
        token = None
        if Authentication.header is not None:
            pass
        else:
            if config.ON_BEHALF_USER:
                authority = config.AUTHORITY_URL + config.TENANT
                context = adal.AuthenticationContext(authority)
                code = context.acquire_user_code(config.RESOURCE, config.CLIENT_ID)
                token = context.acquire_token_with_authorization_code(
                    authorization_code=code,
                    redirect_uri="https://app.getpostman.com/oauth2/callback",
                    resource=config.RESOURCE,
                    client_id=config.CLIENT_ID,
                    client_secret=config.CLIENT_SECRET
                )
            else:
                authority = config.AUTHORITY_URL + config.TENANT
                context = adal.AuthenticationContext(authority)
                token = context.acquire_token_with_client_credentials(
                    config.RESOURCE,
                    config.CLIENT_ID,
                    config.CLIENT_SECRET
                )
        Authentication.header = {'Host': config.BASE,
                                 'Content-Type': "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false",
                                 'Authorization': 'Bearer {0}'.format(token["accessToken"])}

    @staticmethod
    def get_request_specification():
        if Authentication.header is None:
            Authentication()

        return Authentication.header
