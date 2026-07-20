import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from zoko.resources.account import Account
from zoko.resources.agent import Agent
from zoko.resources.customer import Customer
from zoko.resources.group import Group
from zoko.resources.message import Message
from zoko.resources.webhook import Webhook

# Transient statuses worth retrying. 429 included so rate limits back off too.
RETRY_STATUSES = (429, 500, 502, 503, 504)


class ZokoClient:
    def __init__(self, api_key, max_retries=0, backoff_factor=0.5):
        """
        Parameters
        ----------
        api_key
            Zoko API key.
        max_retries
            Number of retries on transient failures (connection errors and the
            5xx/429 statuses in RETRY_STATUSES). Default 0 (no retries). Applies
            to every request, including POST.
        backoff_factor
            Exponential backoff between retries, in seconds
            (sleep = backoff_factor * 2 ** (retry - 1)). Default 0.5.
        """
        if not api_key:
            raise ValueError("API Key is required")
        self.api_key = api_key
        headers = {"apikey": self.api_key, "Content-Type": "application/json"}

        session = requests.Session()
        if max_retries:
            retry = Retry(
                total=max_retries,
                backoff_factor=backoff_factor,
                status_forcelist=RETRY_STATUSES,
                allowed_methods=None,  # retry all methods, POST included
                raise_on_status=False,  # let _request surface the final body as ZokoError
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount("https://", adapter)
            session.mount("http://", adapter)

        self.account = Account(session, headers)
        self.message = Message(session, headers)
        self.customer = Customer(session, headers)
        self.agent = Agent(session, headers)
        self.webhook = Webhook(session, headers)
        self.group = Group(session, headers)
