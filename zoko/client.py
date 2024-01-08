from zoko.resources.account import Account
from zoko.resources.message import Message


class ZokoClient:
    def __init__(self, api_key):
        if api_key is None:
            raise ValueError("API Key is required")
        self.api_key = api_key
        self.__headers = {"apiKey": self.api_key, "Content-Type": "application/json"}
        self.account = Account(self.__headers)
        self.message = Message(self.__headers)
