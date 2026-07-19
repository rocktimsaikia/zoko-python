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

    def test_get_message(self):
        message_id = "3c90c3cc-0d44-4b50-8888-8dd25736052a"
        expected_response = {"id": message_id, "type": "text", "text": "hi"}
        httpretty.register_uri(
            httpretty.GET,
            MessageEndpoint.GET.format(message_id=message_id),
            body=json.dumps(expected_response),
            content_type="application/json",
        )
        response = self.zoko.message.get_message(message_id)
        self.assertEqual(response, expected_response)

    def test_delete_message(self):
        message_id = "3c90c3cc-0d44-4b50-8888-8dd25736052a"
        expected_response = {"id": message_id, "status": "message deleted"}
        httpretty.register_uri(
            httpretty.DELETE,
            MessageEndpoint.DELETE.format(message_id=message_id),
            body=json.dumps(expected_response),
            content_type="application/json",
        )
        response = self.zoko.message.delete_message(message_id)
        self.assertEqual(response, expected_response)

    def test_delete_messages_bulk(self):
        expected_response = {"deleted": 2, "failed": 0, "messages": []}
        httpretty.register_uri(
            httpretty.DELETE,
            MessageEndpoint.BATCH_DELETE,
            body=json.dumps(expected_response),
            content_type="application/json",
        )
        response = self.zoko.message.delete_messages(["id1", "id2"])
        self.assertEqual(response, expected_response)
        sent_body = json.loads(httpretty.last_request().body)
        self.assertEqual(sent_body, {"messages": ["id1", "id2"]})

    def test_send_message_uses_lowercase_apikey_header(self):
        httpretty.register_uri(
            httpretty.POST,
            MessageEndpoint.SEND,
            body=json.dumps({"status": "202"}),
            content_type="application/json",
        )
        self.zoko.message.send_message(
            message="hi", recipient="1234567890", template_type="text"
        )
        self.assertEqual(httpretty.last_request().headers.get("apikey"), "test_api_key")

    def test_send_message_accepts_message_type_enum(self):
        from zoko import MessageType

        httpretty.register_uri(
            httpretty.POST,
            MessageEndpoint.SEND,
            body=json.dumps({"status": "202"}),
            content_type="application/json",
        )
        self.zoko.message.send_message(
            recipient="919998880000",
            template_type=MessageType.BUTTON_TEMPLATE,
            template_id="greeting",
        )
        sent_body = json.loads(httpretty.last_request().body)
        # Enum member must serialize to the raw API string, not "MessageType.X".
        self.assertEqual(sent_body["type"], "buttonTemplate")

    def test_error_raises_zoko_error(self):
        from zoko import ZokoError

        httpretty.register_uri(
            httpretty.POST,
            MessageEndpoint.SEND,
            body=json.dumps({"message": "bad request"}),
            status=400,
            content_type="application/json",
        )
        with self.assertRaises(ZokoError) as ctx:
            self.zoko.message.send_message(
                message="hi", recipient="x", template_type="text"
            )
        self.assertEqual(ctx.exception.status_code, 400)
