# Send a template message
import os

from dotenv import load_dotenv

from zoko import MessageType, ZokoClient

load_dotenv()

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    response = zoko.message.send_message(
        message="hello world",
        recipient="1234567897",
        template_id="_zoko_template_id_",
        template_type=MessageType.TEMPLATE,
    )
    print(response)


if __name__ == "__main__":
    main()
