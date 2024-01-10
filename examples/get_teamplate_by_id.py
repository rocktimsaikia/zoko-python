# Get a template by passing the Zoko template ID
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]
ZOKO_TEMPLATE_ID = "teacher_change_cause_teacher_exit"


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    template = zoko.account.get_template_by_id(template_id=ZOKO_TEMPLATE_ID)
    print(template)


if __name__ == "__main__":
    main()
