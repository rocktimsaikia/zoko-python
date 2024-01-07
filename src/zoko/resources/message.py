import requests
from zoko.constants import endpoint
from typing import Literal, TypedDict


# Parameter types
class Assign(TypedDict):
    assigneeId: str
    ovveride: bool


class WhatsappContactAddress(TypedDict):
    city: str
    country: str
    countryCode: str
    state: str
    street: str
    url: str
    zip: str


class WhatsappContactName(TypedDict):
    firstName: str
    formattedName: str
    lastName: str
    middleName: str
    prefix: str
    suffix: str


class WhatsappContactOrg(TypedDict):
    company: str
    department: str
    title: str


class WhatsappContactsEmail(TypedDict):
    email: str
    type: str


class WhatsappContactsPhone(TypedDict):
    phone: str
    type: str


class WhatsappContacts(TypedDict):
    addresses: list[WhatsappContactAddress]
    emails: list[WhatsappContactsEmail]
    name: WhatsappContactName
    org: WhatsappContactOrg
    phones: list[WhatsappContactsPhone]


class Conatct(TypedDict):
    whatsappContacts: list[WhatsappContacts]


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


# Response types
class SendMessageResponse(TypedDict):
    messageId: str
    status: str
    statusText: str


class Message:
    def __init__(self, __header):
        self.header = __header

    def send_message(
        self,
        assign: Assign,
        message: str,
        caption: str,
        send_to: str,
        template_id: str,
        template_args: list[str],
        template_type: TemplateType,
        template_language: str,
    ) -> SendMessageResponse:
        payload = {
            "assign": assign,
            "channel": "whatsapp",
            "message": message,
            "caption": caption,
            "recipient": send_to,
            "templateId": template_id,
            "templateArgs": template_args,
            "templateLanguage": template_language,
            "type": template_type,
        }
        response = requests.request(
            "POST",
            endpoint.MessageEndpoint.SEND,
            headers=self.header,
            json=payload,
        )
        response_json = response.json()
        return response_json
