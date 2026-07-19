from typing import Literal

Channel = Literal["whatsapp"]

CustomerPropertyType = Literal["text", "image", "document", "video"]

AgentRole = Literal["owner", "admin", "salesman"]

WebhookEvent = Literal[
    "message:user:in",
    "message:store:out",
    "message:delivery:update",
]

JoinRequestAction = Literal["approve", "reject"]

TemplateType = Literal[
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
]
