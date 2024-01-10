# Get all templates from your Zoko account
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()


ZOKO_API_KEY = os.environ.get("ZOKO_API_KEY")

print("ZOKO_API_KEY", ZOKO_API_KEY)


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    templates = zoko.account.get_all_templates()
    print(templates)


if __name__ == "__main__":
    main()
