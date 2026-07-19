# Webhook resource - manage event webhooks
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])

WEBHOOK_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


def main():
    # create_webhook -> {"id": ..., "url": ..., "events": [...], "challengeToken": ...}
    created = zoko.webhook.create_webhook(
        url="https://example.com/zoko-hook",
        events=["message:user:in", "message:delivery:update"],
        challenge_token="my_secret",
    )
    print(created)

    # get_webhooks -> [{"id": ..., "url": ..., "events": [...]}, ...]
    webhooks = zoko.webhook.get_webhooks()
    print(webhooks)

    # get_webhook -> {"id": ..., "url": ..., "events": [...]}
    zoko.webhook.get_webhook(WEBHOOK_ID)

    # update_webhook (url and events required) -> {"id": ..., "url": ..., "events": [...]}
    zoko.webhook.update_webhook(
        WEBHOOK_ID,
        url="https://example.com/zoko-hook-v2",
        events=["message:user:in"],
    )

    # delete_webhook -> {"status": "204", ...}
    zoko.webhook.delete_webhook(WEBHOOK_ID)


if __name__ == "__main__":
    main()
