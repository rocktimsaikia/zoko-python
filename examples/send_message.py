# Get a template by passing the Zoko template ID
import os
from zoko import ZokoClient

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)
    payload = {
        "message": "hello world",
        "recipient": "1234567890",
        "template_id": "greeting_01",
        "template_args": ["John", "Doe"],
        "template_language": "en",
        "template_type": "buttonTemplate",
    }
    response = zoko.message.send_message(**payload)
    print(response)
    # {
    #     "messageId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    #     "status": "202",
    #     "statusText": "Accepted",
    # }


if __name__ == "__main__":
    main()
