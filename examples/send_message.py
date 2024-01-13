# Get a template by passing the Zoko template ID
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    payload = {
        "message": "hello world",
        "recipient": "1234567897",
        "template_id": "_zoko_template_id_",
        "template_type": "template",
    }
    response = zoko.message.send_message(**payload)
    print(response)


if __name__ == "__main__":
    main()
