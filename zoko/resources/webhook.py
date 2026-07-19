from typing import List, Optional, TypedDict

from zoko.constants.endpoint import WebhookEndpoint
from zoko.resources.base import Resource
from zoko.types.common import WebhookEvent


class WebhookDetails(TypedDict):
    id: str
    url: str
    challengeToken: str
    events: List[str]


class Webhook(Resource):
    def get_webhooks(self) -> List[WebhookDetails]:
        """Retrieve all webhooks for the account."""
        return self._request("GET", WebhookEndpoint.LIST)

    def create_webhook(
        self,
        url: str,
        events: List[WebhookEvent],
        challenge_token: Optional[str] = None,
    ) -> WebhookDetails:
        """
        Create a new webhook.

        Parameters
        ----------
        url
            The URL to receive webhook events.
        events
            Events to subscribe to (at least one). Values from WebhookEvent.
        challenge_token
            Optional challenge token (<= 200 characters).
        """
        if not url:
            raise ValueError("Webhook URL is required")
        if not events:
            raise ValueError("At least one event is required")
        payload = self._clean(
            {"url": url, "events": events, "challengeToken": challenge_token}
        )
        return self._request("POST", WebhookEndpoint.CREATE, json=payload)

    def get_webhook(self, webhook_id: str) -> WebhookDetails:
        """Retrieve webhook details."""
        if not webhook_id:
            raise ValueError("Webhook ID is required")
        url = WebhookEndpoint.GET.format(webhook_id=webhook_id)
        return self._request("GET", url)

    def update_webhook(
        self,
        webhook_id: str,
        url: str,
        events: List[WebhookEvent],
        challenge_token: Optional[str] = None,
    ) -> WebhookDetails:
        """
        Update webhook details. url and events are required by the API.
        """
        if not webhook_id:
            raise ValueError("Webhook ID is required")
        if not url:
            raise ValueError("Webhook URL is required")
        if not events:
            raise ValueError("At least one event is required")
        endpoint = WebhookEndpoint.UPDATE.format(webhook_id=webhook_id)
        payload = self._clean(
            {"url": url, "events": events, "challengeToken": challenge_token}
        )
        return self._request("PUT", endpoint, json=payload)

    def delete_webhook(self, webhook_id: str) -> dict:
        """Delete an existing webhook."""
        if not webhook_id:
            raise ValueError("Webhook ID is required")
        endpoint = WebhookEndpoint.DELETE.format(webhook_id=webhook_id)
        return self._request("DELETE", endpoint)
