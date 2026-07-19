import json
import unittest

import httpretty

from zoko.client import ZokoClient
from zoko.constants.endpoint import CustomerEndpoint

CUSTOMER_ID = "3c90c3cc-0d44-4b50-8888-8dd25736052a"
PROPERTY_ID = "aa11bb22-0d44-4b50-8888-8dd25736052a"


class TestZokoClientCustomer(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_get_customers_sends_channel_query(self):
        expected = {"currentPage": 1, "totalCustomers": 0, "customers": []}
        httpretty.register_uri(
            httpretty.GET,
            CustomerEndpoint.LIST,
            body=json.dumps(expected),
            content_type="application/json",
        )
        response = self.zoko.customer.get_customers(channel="whatsapp", page_size=10)
        self.assertEqual(response, expected)
        qs = httpretty.last_request().querystring
        self.assertEqual(qs["channel"], ["whatsapp"])
        self.assertEqual(qs["pageSize"], ["10"])

    def test_get_customer(self):
        expected = {"id": CUSTOMER_ID, "name": "Jane"}
        httpretty.register_uri(
            httpretty.GET,
            CustomerEndpoint.GET.format(customer_id=CUSTOMER_ID),
            body=json.dumps(expected),
            content_type="application/json",
        )
        self.assertEqual(self.zoko.customer.get_customer(CUSTOMER_ID), expected)

    def test_create_property_strips_none(self):
        httpretty.register_uri(
            httpretty.POST,
            CustomerEndpoint.CREATE_PROPERTY.format(customer_id=CUSTOMER_ID),
            body=json.dumps({"status": "204"}),
            content_type="application/json",
        )
        self.zoko.customer.create_property(
            CUSTOMER_ID, type="text", title="VIP"
        )
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"type": "text", "title": "VIP"})

    def test_add_tag_sends_query(self):
        httpretty.register_uri(
            httpretty.POST,
            CustomerEndpoint.ADD_TAG.format(customer_id=CUSTOMER_ID),
            body=json.dumps([{"status": "200"}]),
            content_type="application/json",
        )
        self.zoko.customer.add_tag(CUSTOMER_ID, "vip")
        self.assertEqual(httpretty.last_request().querystring["tag"], ["vip"])

    def test_update_tags_bulk(self):
        httpretty.register_uri(
            httpretty.PUT,
            CustomerEndpoint.UPDATE_TAGS.format(customer_id=CUSTOMER_ID),
            body=json.dumps([{"status": "200"}]),
            content_type="application/json",
        )
        self.zoko.customer.update_tags(CUSTOMER_ID, ["a", "b"])
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"tags": ["a", "b"]})

    def test_assign_customer(self):
        httpretty.register_uri(
            httpretty.POST,
            CustomerEndpoint.ASSIGN_CUSTOMER.format(customer_id=CUSTOMER_ID),
            body=json.dumps({"status": "200"}),
            content_type="application/json",
        )
        self.zoko.customer.assign_customer(CUSTOMER_ID, assignee_id="agent1")
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"id": CUSTOMER_ID, "assigneeId": "agent1"})

    def test_get_property_requires_ids(self):
        with self.assertRaises(ValueError):
            self.zoko.customer.get_property(CUSTOMER_ID, "")


if __name__ == "__main__":
    unittest.main()
