# Get a template by passing the Zoko template ID
import os
from zoko import ZokoClient

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    templates = zoko.account.get_template_by_id(template_id="ZOKO_TEMPLATE_ID")
    print(templates)


if __name__ == "__main__":
    main()
