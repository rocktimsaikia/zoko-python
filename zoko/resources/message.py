from typing import List, Optional, TypedDict

from zoko.constants.endpoint import MessageEndpoint
from zoko.resources.base import Resource
from zoko.types.common import TemplateType


# Parameter types
class Assign(TypedDict):
    assigneeId: str
    override: bool


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


class DeleteMessageResponse(TypedDict):
    id: str
    status: str
    description: str


class BulkDeleteResponse(TypedDict):
    deleted: int
    failed: int
    messages: List[DeleteMessageResponse]


class Message(Resource):
    def send_message(
        self,
        message: Optional[str] = None,
        recipient: str = None,
        template_id: Optional[str] = None,
        template_type: TemplateType = None,
        template_language: str = "en",
        template_args: Optional[List[str]] = None,
        assign: Optional[Assign] = None,
        caption: Optional[str] = None,
        contacts: Optional[Contact] = None,
    ) -> SendMessageResponse:
        """
        Send message to customer on a specific channel.

        Parameters
        ----------
        message
            Content of the message. For text messages this is the text;
            for media types (image, document, audio, video, sticker) it is the
            file URL; for location it is "<latitude>:<longitude>". Not used for
            template/richTemplate/buttonTemplate/contacts types.
        recipient
            E.164 formatted whatsapp number without the leading "+" sign.
        template_id
            Template ID. Mandatory for template, richTemplate and buttonTemplate.
        template_type
            The message type. One of the values in TemplateType.
        template_language
            Template language. Defaults to "en".
        template_args
            Template placeholder values in the same order as in the template.
        assign (optional)
            Assign the chat to a specific agent.
        caption (optional)
            Describes the specified image, video or document media (not audio).
        contacts (optional)
            Contacts array for message type contacts.

        Returns
        -------
        SendMessageResponse
            The response object with the message ID and status.
        """
        payload = self._clean(
            {
                "channel": "whatsapp",
                "recipient": recipient,
                "type": template_type,
                "message": message,
                "caption": caption,
                "templateId": template_id,
                "templateArgs": template_args,
                "templateLanguage": template_language,
                "assign": assign,
                "contacts": contacts,
            }
        )
        return self._request("POST", MessageEndpoint.SEND, json=payload)

    def get_message(self, message_id: str) -> dict:
        """
        Retrieve message details.

        Parameters
        ----------
        message_id
            The ID of the message to fetch.
        """
        if not message_id:
            raise ValueError("Message ID is required")
        url = MessageEndpoint.GET.format(message_id=message_id)
        return self._request("GET", url)

    def delete_message(self, message_id: str) -> DeleteMessageResponse:
        """
        Delete a message from the Zoko database.

        Note: Deletion is only from the Zoko database and does not affect the
        message on the customer's client application.

        Parameters
        ----------
        message_id
            The ID of the message to delete.
        """
        if not message_id:
            raise ValueError("Message ID is required")
        url = MessageEndpoint.DELETE.format(message_id=message_id)
        return self._request("DELETE", url)

    def get_message_history(self, message_id: str) -> dict:
        """
        Retrieve message delivery history.

        Parameters
        ----------
        message_id
            The ID of the message.
        """
        if not message_id:
            raise ValueError("Message ID is required")
        url = MessageEndpoint.HISTORY.format(message_id=message_id)
        return self._request("GET", url)

    def delete_messages(self, message_ids: List[str]) -> BulkDeleteResponse:
        """
        Delete a set of messages (1-50) from the Zoko database.

        Parameters
        ----------
        message_ids
            IDs of the messages to delete. Must contain between 1 and 50 IDs.
        """
        if not message_ids:
            raise ValueError("At least one message ID is required")
        payload = {"messages": message_ids}
        return self._request("DELETE", MessageEndpoint.BATCH_DELETE, json=payload)
