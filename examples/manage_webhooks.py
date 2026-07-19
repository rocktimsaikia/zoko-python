# Create a webhook and list all webhooks
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)

    created = zoko.webhook.create_webhook(
        url="https://example.com/zoko-hook",
        events=["message:user:in", "message:delivery:update"],
        challenge_token="my_secret",
    )
    print(f"Created webhook {created['id']}")

    for hook in zoko.webhook.get_webhooks():
        print(hook["url"], hook["events"])


if __name__ == "__main__":
    main()
