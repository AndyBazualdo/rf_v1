import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import re


class EndPointHelper:

    @staticmethod
    def build_endpoint(endpoint, context):
        endpoint_split = str(endpoint).split("/")

        for i in range(len(endpoint_split)):
            if endpoint_split[i].__contains__("{"):
                reg_exp = "(?={)(.*?)(}=?)"
                if type(context) is dict:
                    endpoint_split[i] = re.sub(reg_exp, context.values()[len(context) - 1], endpoint_split[i])
                else:
                    endpoint_split[i] = re.sub(reg_exp, context, endpoint_split[i])
        return "/".join(endpoint_split)
