import json
import unittest

import httpretty

from zoko.client import ZokoClient
from zoko.constants.endpoint import GROUP, GroupEndpoint

GROUP_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestZokoClientGroup(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_group_base_path(self):
        self.assertEqual(GROUP, "https://chat.zoko.io/v2/channels/whatsapp/cloud/group")

    def test_create_group(self):
        httpretty.register_uri(
            httpretty.POST,
            GroupEndpoint.CREATE,
            body=json.dumps({"_id": GROUP_ID, "status": "pending"}),
            content_type="application/json",
        )
        self.zoko.group.create_group(subject="My Group")
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"subject": "My Group"})

    def test_handle_join_requests_action_in_path(self):
        httpretty.register_uri(
            httpretty.POST,
            GroupEndpoint.HANDLE_JOIN_REQUESTS.format(
                group_id=GROUP_ID, action="approve"
            ),
            body=json.dumps({"status": "ok"}),
            content_type="application/json",
        )
        self.zoko.group.handle_join_requests(GROUP_ID, "approve", ["jr1", "jr2"])
        self.assertTrue(
            httpretty.last_request().path.endswith("/join-requests/approve")
        )
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"join_requests": ["jr1", "jr2"]})

    def test_handle_join_requests_rejects_bad_action(self):
        with self.assertRaises(ValueError):
            self.zoko.group.handle_join_requests(GROUP_ID, "maybe", ["jr1"])

    def test_delete_group_uses_post(self):
        httpretty.register_uri(
            httpretty.POST,
            GroupEndpoint.DELETE.format(group_id=GROUP_ID),
            body=json.dumps({"status": "ok"}),
            content_type="application/json",
        )
        self.zoko.group.delete_group(GROUP_ID)
        self.assertTrue(httpretty.last_request().path.endswith("/delete"))

    def test_set_auto_approval(self):
        httpretty.register_uri(
            httpretty.PUT,
            GroupEndpoint.AUTO_APPROVAL.format(group_id=GROUP_ID),
            body=json.dumps({"status": "ok"}),
            content_type="application/json",
        )
        self.zoko.group.set_auto_approval(GROUP_ID, True)
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"auto_approval": True})

    def test_invite_members_requires_numbers(self):
        with self.assertRaises(ValueError):
            self.zoko.group.invite_members(GROUP_ID, [])


if __name__ == "__main__":
    unittest.main()
