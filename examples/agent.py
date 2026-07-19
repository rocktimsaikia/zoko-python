# Agent resource - agents and teams
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])

# Agent id can be a UUID or the agent's email
AGENT_ID = "agent@example.com"


def main():
    # get_agent -> {"id": ..., "email": ..., "role": ..., "active": True, ...}
    agent = zoko.agent.get_agent(AGENT_ID, include_teams=True)
    print(agent)

    # update_agent -> {"id": ..., "role": "admin", "available": False, ...}
    zoko.agent.update_agent(AGENT_ID, role="admin", available=False)

    # get_agents -> [{"id": ..., "email": ..., "role": ...}, ...]
    agents = zoko.agent.get_agents(include_teams=True)
    print(agents)

    # get_teams -> [{"id": ..., "name": ..., "memberCount": N}, ...]
    teams = zoko.agent.get_teams(include_agents=True)
    print(teams)


if __name__ == "__main__":
    main()
