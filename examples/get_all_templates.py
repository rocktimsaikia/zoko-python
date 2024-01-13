# Get all templates from your Zoko account
import json
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()


ZOKO_API_KEY = os.environ.get("ZOKO_API_KEY")


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    all_templates = zoko.account.get_all_templates()

    # Pretty print the JSON response
    print(json.dumps(all_templates, indent=2))


if __name__ == "__main__":
    main()
