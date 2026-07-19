import json
import unittest

import httpretty

from zoko.client import ZokoClient
from zoko.constants.endpoint import WebhookEndpoint

WEBHOOK_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestZokoClientWebhook(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_get_webhooks(self):
        expected = [{"id": WEBHOOK_ID, "url": "https://x.com", "events": []}]
        httpretty.register_uri(
            httpretty.GET,
            WebhookEndpoint.LIST,
            body=json.dumps(expected),
            content_type="application/json",
        )
        self.assertEqual(self.zoko.webhook.get_webhooks(), expected)

    def test_create_webhook(self):
        httpretty.register_uri(
            httpretty.POST,
            WebhookEndpoint.CREATE,
            body=json.dumps({"id": WEBHOOK_ID}),
            content_type="application/json",
        )
        self.zoko.webhook.create_webhook(
            url="https://x.com", events=["message:user:in"]
        )
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"url": "https://x.com", "events": ["message:user:in"]})

    def test_delete_webhook(self):
        httpretty.register_uri(
            httpretty.DELETE,
            WebhookEndpoint.DELETE.format(webhook_id=WEBHOOK_ID),
            body=json.dumps({"status": "204"}),
            content_type="application/json",
        )
        self.zoko.webhook.delete_webhook(WEBHOOK_ID)
        self.assertTrue(
            httpretty.last_request().path.endswith("/webhook/" + WEBHOOK_ID)
        )

    def test_create_webhook_requires_events(self):
        with self.assertRaises(ValueError):
            self.zoko.webhook.create_webhook(url="https://x.com", events=[])


if __name__ == "__main__":
    unittest.main()
