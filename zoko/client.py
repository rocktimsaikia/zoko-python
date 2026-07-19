from zoko.resources.account import Account
from zoko.resources.agent import Agent
from zoko.resources.customer import Customer
from zoko.resources.group import Group
from zoko.resources.message import Message
from zoko.resources.webhook import Webhook


class ZokoClient:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API Key is required")
        self.api_key = api_key
        headers = {"apikey": self.api_key, "Content-Type": "application/json"}
        self.account = Account(headers)
        self.message = Message(headers)
        self.customer = Customer(headers)
        self.agent = Agent(headers)
        self.webhook = Webhook(headers)
        self.group = Group(headers)
