# Message resource - send and manage messages
import os

from dotenv import load_dotenv

from zoko import MessageType, ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])

MESSAGE_ID = "3c90c3cc-0d44-4b50-8888-8dd25736052a"


def main():
    # send_message -> {"status": "202", "statusText": "Accepted", "messageId": ...}
    sent = zoko.message.send_message(
        recipient="919998880000",
        template_type=MessageType.TEMPLATE,
        template_id="greeting_01",
        template_args=["John"],
    )
    print(sent)

    # A plain text message (no template)
    zoko.message.send_message(
        recipient="919998880000",
        template_type=MessageType.TEXT,
        message="Hi there! How can we help?",
    )

    # get_message -> {"id": ..., "type": ..., "text": ..., "deliveryStatus": ..., ...}
    message = zoko.message.get_message(MESSAGE_ID)
    print(message)

    # get_message_history -> {"messageId": ..., "history": [...]}
    history = zoko.message.get_message_history(MESSAGE_ID)
    print(history)

    # delete_message -> {"id": ..., "status": "message deleted", ...}
    zoko.message.delete_message(MESSAGE_ID)

    # delete_messages (bulk, 1-50 ids) -> {"deleted": 2, "failed": 0, "messages": [...]}
    zoko.message.delete_messages([MESSAGE_ID, "another-message-id"])


if __name__ == "__main__":
    main()
