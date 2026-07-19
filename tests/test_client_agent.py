import json
import unittest

import httpretty

from zoko.client import ZokoClient
from zoko.constants.endpoint import AgentEndpoint

AGENT_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestZokoClientAgent(unittest.TestCase):
    def setUp(self):
        self.zoko = ZokoClient(api_key="test_api_key")
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_get_agent_with_include_teams(self):
        expected = {"id": AGENT_ID, "email": "a@b.com", "role": "admin"}
        httpretty.register_uri(
            httpretty.GET,
            AgentEndpoint.GET.format(agent_id=AGENT_ID),
            body=json.dumps(expected),
            content_type="application/json",
        )
        response = self.zoko.agent.get_agent(AGENT_ID, include_teams=True)
        self.assertEqual(response, expected)
        self.assertEqual(httpretty.last_request().querystring["includeTeams"], ["True"])

    def test_get_agents_uses_agents_path(self):
        httpretty.register_uri(
            httpretty.GET,
            AgentEndpoint.LIST_AGENTS,
            body=json.dumps([{"id": AGENT_ID}]),
            content_type="application/json",
        )
        response = self.zoko.agent.get_agents()
        self.assertEqual(response, [{"id": AGENT_ID}])
        self.assertTrue(httpretty.last_request().path.endswith("/agent/agents"))

    def test_get_teams_uses_teams_path(self):
        httpretty.register_uri(
            httpretty.GET,
            AgentEndpoint.LIST_TEAMS,
            body=json.dumps([{"id": "team1"}]),
            content_type="application/json",
        )
        self.zoko.agent.get_teams()
        self.assertTrue(httpretty.last_request().path.startswith("/v2/agent/teams"))

    def test_update_agent(self):
        httpretty.register_uri(
            httpretty.PUT,
            AgentEndpoint.UPDATE.format(agent_id=AGENT_ID),
            body=json.dumps({"id": AGENT_ID, "role": "salesman"}),
            content_type="application/json",
        )
        self.zoko.agent.update_agent(AGENT_ID, role="salesman", available=False)
        body = json.loads(httpretty.last_request().body)
        self.assertEqual(body, {"id": AGENT_ID, "role": "salesman", "available": False})


if __name__ == "__main__":
    unittest.main()
