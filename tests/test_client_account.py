import unittest
from zoko.client import ZokoClient
from zoko.constants.endpoint import AccountEndpoint
import httpretty
import json


class TestZokoClient(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def test_api_key_required(self):
        with self.assertRaises(ValueError):
            ZokoClient(api_key=None)

    def test_get_all_templates(self):
        expected_response = [
            {
                "active": True,
                "channel": "whatsapp",
                "isRichTemplate": True,
                "templateDesc": "Good morning {{1}}. How may I help you today?",
                "templateId": "greeting_01",
                "templateLanguage": "en",
                "templateType": "<string>",
                "templateVariableCount": 1,
            }
        ]
        httpretty.register_uri(
            httpretty.GET,
            AccountEndpoint.TEMPLATES,
            body=json.dumps(expected_response),
            content_type="application/json",
        )

        response = self.zoko.account.get_all_templates()
        self.assertEqual(response, expected_response)

    def test_get_template_by_id(self):
        expected_response = [
            {
                "active": True,
                "channel": "whatsapp",
                "isRichTemplate": True,
                "templateDesc": "Good morning {{1}}. How may I help you today?",
                "templateId": "greeting_01",
                "templateLanguage": "en",
                "templateType": "<string>",
                "templateVariableCount": 1,
            },
            {
                "active": True,
                "channel": "whatsapp",
                "isRichTemplate": True,
                "templateDesc": "Good evening {{1}}. How may I help you today?",
                "templateId": "greeting_02",
                "templateLanguage": "en",
                "templateType": "<string>",
                "templateVariableCount": 1,
            },
        ]
        httpretty.register_uri(
            httpretty.GET,
            AccountEndpoint.TEMPLATES,
            body=json.dumps(expected_response),
            content_type="application/json",
        )
        response = self.zoko.account.get_template_by_id(template_id="greeting_01")
        self.assertEqual(response, expected_response[0])
