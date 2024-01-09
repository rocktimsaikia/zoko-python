# Get all templates from your Zoko account
import os
from zoko import ZokoClient

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    templates = zoko.account.get_all_templates()
    print(templates)


if __name__ == "__main__":
    main()