import requests
from zoko.constants.endpoint import MessageEndpoint
from typing import TypedDict, List, Optional

from zoko.types.common import TemplateType


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
    addresses: List[WhatsappContactAddress]
    emails: List[WhatsappContactsEmail]
    name: WhatsappContactName
    org: WhatsappContactOrg
    phones: List[WhatsappContactsPhone]


class Contact(TypedDict):
    whatsappContacts: List[WhatsappContacts]


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
        message: str,
        recipient: str,
        template_id: str,
        template_args: list[str],
        template_type: TemplateType,
        template_language: str = "en",
        assign: Optional[Assign] = None,
        caption: Optional[str] = None,
        contacts: Optional[Contact] = None,
    ) -> SendMessageResponse:
        """
        Send message to customer on a specific channel.

        Parameters
        ----------
        assign (optional)
            Assign the chat to a specific agent.
        message
            Content of the message.
        caption (optional)
            Describe of the specified "image", "video" or "document" media except for "audio".
        contacts (optional)
            Contacts array for message type contacts.
        recipient
            E.164 formatted whatsapp number without the leading "+" sign.
        template_id
            Template ID to be used.
        template_args
            Template placeholder values in the same order as in the template.
        template_type
            The type of the template.
        template_language
            The language of the template.

        Returns
        -------
        SendMessageResponse
            The response object with the message ID and status.
        """
        payload = {
            "assign": assign,
            "channel": "whatsapp",
            "message": message,
            "caption": caption,
            "contacts": contacts,
            "recipient": recipient,
            "templateId": template_id,
            "templateArgs": template_args,
            "templateLanguage": template_language,
            "type": template_type,
        }
        response = requests.request(
            "POST",
            MessageEndpoint.SEND,
            headers=self.header,
            json=payload,
        )
        response_json = response.json()
        return response_json
