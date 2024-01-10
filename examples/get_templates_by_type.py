# Filter templates by type
import json
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()


ZOKO_API_KEY = os.environ.get("ZOKO_API_KEY")

print("ZOKO_API_KEY", ZOKO_API_KEY)


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    button_templates = zoko.account.get_templates_by_type("buttonTemplate")

    # Pretty print the JSON response
    print(json.dumps(button_templates, indent=2))


if __name__ == "__main__":
    main()
