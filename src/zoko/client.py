from zoko.resources.account import Account


class ZokoClient:
    def __init__(self, api_key):
        if api_key is None:
            raise ValueError("API Key is required")
        self.api_key = api_key
        self.__headers = {"apiKey": self.api_key}
        self.account = Account(self.__headers)
