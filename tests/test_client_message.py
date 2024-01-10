import json
import unittest

import httpretty

from zoko.client import ZokoClient
from zoko.constants.endpoint import MessageEndpoint


class TestZokoClientMessage(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def test_send_message_success(self):
        expected_response = {
            "messageId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "status": "202",
            "statusText": "Accepted",
        }
        httpretty.register_uri(
            httpretty.POST,
            MessageEndpoint.SEND,
            body=json.dumps(expected_response),
            content_type="application/json",
        )
        payload = {
            "message": "hello world",
            "recipient": "1234567890",
            "template_id": "greeting_01",
            "template_args": ["John", "Doe"],
            "template_language": "en",
            "template_type": "buttonTemplate",
        }
        response = self.zoko.message.send_message(**payload)
        self.assertEqual(response, expected_response)
        self.assertIn("messageId", response)
        self.assertIn("status", response)
        self.assertIn("statusText", response)
