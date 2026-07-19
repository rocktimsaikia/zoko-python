from typing import List, Optional, TypedDict

from zoko.constants.endpoint import AgentEndpoint
from zoko.resources.base import Resource
from zoko.types.common import AgentRole


class AgentDetails(TypedDict):
    id: str
    firstName: str
    lastName: str
    email: str
    role: str
    active: bool
    available: bool


class Team(TypedDict):
    id: str
    name: str
    description: str
    active: bool
    memberCount: int


class Agent(Resource):
    def get_agent(self, agent_id: str, include_teams: Optional[bool] = None) -> AgentDetails:
        """
        Retrieve agent details.

        Parameters
        ----------
        agent_id
            ID or email of the agent.
        include_teams
            Include teams where the agent is a member.
        """
        if not agent_id:
            raise ValueError("Agent ID is required")
        url = AgentEndpoint.GET.format(agent_id=agent_id)
        params = self._clean({"includeTeams": include_teams})
        return self._request("GET", url, params=params)

    def update_agent(
        self,
        agent_id: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        role: Optional[AgentRole] = None,
        active: Optional[bool] = None,
        available: Optional[bool] = None,
    ) -> AgentDetails:
        """
        Update an existing agent's role and availability.

        Parameters
        ----------
        agent_id
            ID or email of the agent.
        role
            One of "owner", "admin" or "salesman".
        """
        if not agent_id:
            raise ValueError("Agent ID is required")
        url = AgentEndpoint.UPDATE.format(agent_id=agent_id)
        payload = self._clean(
            {
                "id": agent_id,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "role": role,
                "active": active,
                "available": available,
            }
        )
        return self._request("PUT", url, json=payload)

    def get_agents(self, include_teams: Optional[bool] = None) -> List[AgentDetails]:
        """
        Retrieve the agents list.

        Parameters
        ----------
        include_teams
            Include teams where each agent is a member.
        """
        params = self._clean({"includeTeams": include_teams})
        return self._request("GET", AgentEndpoint.LIST_AGENTS, params=params)

    def get_teams(self, include_agents: Optional[bool] = None) -> List[Team]:
        """
        Retrieve the teams list.

        Parameters
        ----------
        include_agents
            Include the agents of each team.
        """
        params = self._clean({"includeAgents": include_agents})
        return self._request("GET", AgentEndpoint.LIST_TEAMS, params=params)
