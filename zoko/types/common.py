from enum import Enum
from typing import Literal, Union


class MessageType(str, Enum):
    """Message types accepted by ``send_message``.

    Members are ``str`` values, so ``MessageType.TEXT`` can be used anywhere the
    raw ``"text"`` string is expected (it serializes to ``"text"`` on the wire).
    """

    TEXT = "text"
    IMAGE = "image"
    DOCUMENT = "document"
    AUDIO = "audio"
    VIDEO = "video"
    LOCATION = "location"
    STICKER = "sticker"
    CONTACTS = "contacts"
    TEMPLATE = "template"
    RICH_TEMPLATE = "richTemplate"
    BUTTON_TEMPLATE = "buttonTemplate"


Channel = Literal["whatsapp"]

CustomerPropertyType = Literal["text", "image", "document", "video"]

AgentRole = Literal["owner", "admin", "salesman"]

WebhookEvent = Literal[
    "message:user:in",
    "message:store:out",
    "message:delivery:update",
]

JoinRequestAction = Literal["approve", "reject"]

# Kept for type hints; accepts a MessageType member or the raw string.
TemplateType = Union[
    MessageType,
    Literal[
        "text",
        "image",
        "document",
        "audio",
        "video",
        "location",
        "sticker",
        "contacts",
        "template",
        "richTemplate",
        "buttonTemplate",
    ],
]
