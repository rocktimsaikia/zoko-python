# Account resource - message templates
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])


def main():
    # get_all_templates -> [{"templateId": ..., "templateType": ..., "active": True, ...}, ...]
    templates = zoko.account.get_all_templates()
    print(templates)

    # get_template_by_id -> {"templateId": "greeting_01", "templateType": ..., ...}
    template = zoko.account.get_template_by_id("greeting_01")
    print(template)

    # get_templates_by_type -> [{"templateType": "buttonTemplate", ...}, ...]
    button_templates = zoko.account.get_templates_by_type("buttonTemplate")
    print(button_templates)


if __name__ == "__main__":
    main()
