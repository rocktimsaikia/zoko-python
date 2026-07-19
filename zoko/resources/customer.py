from typing import List, Optional, TypedDict

from zoko.constants.endpoint import CustomerEndpoint
from zoko.resources.base import Resource
from zoko.types.common import Channel, CustomerPropertyType


# Response / parameter types
class CustomerProperty(TypedDict):
    id: str
    entityType: str
    entityId: str
    type: str
    title: str
    description: str
    messages: List[str]
    priority: int


class CustomerTags(TypedDict):
    entityId: str
    entityType: str
    tags: List[str]


class StatusResponse(TypedDict):
    status: str
    message: str
    details: str


class Customer(Resource):
    def get_customers(
        self,
        channel: Channel = "whatsapp",
        page: Optional[str] = None,
        page_size: Optional[int] = None,
        include_assign: Optional[bool] = None,
        sort_by: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> dict:
        """
        Retrieve the customer list.

        Parameters
        ----------
        channel
            Customer channel. Required. Currently only "whatsapp".
        page
            Page number (for pagination).
        page_size
            Page size (for pagination).
        include_assign
            Include assignment details. Default is False.
        sort_by
            Sort field: "name", "lastIncomingMessageAt" or "contactable".
        order_by
            Sort order: "asc" or "desc".
        """
        params = self._clean(
            {
                "channel": channel,
                "page": page,
                "pageSize": page_size,
                "includeAssign": include_assign,
                "sortBy": sort_by,
                "orderBy": order_by,
            }
        )
        return self._request("GET", CustomerEndpoint.LIST, params=params)

    def get_customer(self, customer_id: str) -> dict:
        """Retrieve customer details."""
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.GET.format(customer_id=customer_id)
        return self._request("GET", url)

    def delete_messages(self, customer_id: str) -> StatusResponse:
        """
        Delete all messages for a customer (from the Zoko database only).

        Note: Deletion does not affect the messages on the customer's client
        application.
        """
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.DELETE.format(customer_id=customer_id)
        return self._request("DELETE", url)

    # Properties
    def list_properties(self, customer_id: str) -> List[CustomerProperty]:
        """List all properties of a customer."""
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.LIST_PROPERTIES.format(customer_id=customer_id)
        return self._request("GET", url)

    def create_property(
        self,
        customer_id: str,
        type: CustomerPropertyType,
        title: Optional[str] = None,
        description: Optional[str] = None,
        messages: Optional[List[str]] = None,
        priority: Optional[int] = None,
    ) -> StatusResponse:
        """
        Create a customer property.

        Parameters
        ----------
        customer_id
            ID of the customer.
        type
            Property type: "text", "image", "document" or "video".
        title
            Property title.
        description
            Details on the property.
        messages
            URL(s) for type image/document/video; text for type text.
        priority
            Order in which it is displayed on the web app.
        """
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.CREATE_PROPERTY.format(customer_id=customer_id)
        payload = self._clean(
            {
                "type": type,
                "title": title,
                "description": description,
                "messages": messages,
                "priority": priority,
            }
        )
        return self._request("POST", url, json=payload)

    def get_property(self, customer_id: str, property_id: str) -> CustomerProperty:
        """Get customer property details."""
        if not customer_id or not property_id:
            raise ValueError("Customer ID and property ID are required")
        url = CustomerEndpoint.GET_PROPERTY.format(
            customer_id=customer_id, property_id=property_id
        )
        return self._request("GET", url)

    def update_property(
        self,
        customer_id: str,
        property_id: str,
        type: Optional[CustomerPropertyType] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        messages: Optional[List[str]] = None,
        priority: Optional[int] = None,
    ) -> CustomerProperty:
        """Update customer property details."""
        if not customer_id or not property_id:
            raise ValueError("Customer ID and property ID are required")
        url = CustomerEndpoint.UPDATE_PROPERTY.format(
            customer_id=customer_id, property_id=property_id
        )
        payload = self._clean(
            {
                "type": type,
                "title": title,
                "description": description,
                "messages": messages,
                "priority": priority,
            }
        )
        return self._request("PUT", url, json=payload)

    def delete_property(self, customer_id: str, property_id: str) -> StatusResponse:
        """Delete a customer property."""
        if not customer_id or not property_id:
            raise ValueError("Customer ID and property ID are required")
        url = CustomerEndpoint.DELETE_PROPERTY.format(
            customer_id=customer_id, property_id=property_id
        )
        return self._request("DELETE", url)

    # Tags
    def list_tags(self, customer_id: str) -> CustomerTags:
        """List all tags of a customer."""
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.LIST_TAGS.format(customer_id=customer_id)
        return self._request("GET", url)

    def update_tags(self, customer_id: str, tags: List[str]) -> List[StatusResponse]:
        """
        Replace the customer's entire tag list with the provided list.
        """
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.UPDATE_TAGS.format(customer_id=customer_id)
        return self._request("PUT", url, json={"tags": tags})

    def add_tag(self, customer_id: str, tag: str) -> List[StatusResponse]:
        """Add a single tag to a customer."""
        if not customer_id:
            raise ValueError("Customer ID is required")
        if not tag:
            raise ValueError("Tag is required")
        url = CustomerEndpoint.ADD_TAG.format(customer_id=customer_id)
        return self._request("POST", url, params={"tag": tag})

    def delete_tag(self, customer_id: str, tag: str) -> List[StatusResponse]:
        """Delete a single tag from a customer."""
        if not customer_id:
            raise ValueError("Customer ID is required")
        if not tag:
            raise ValueError("Tag is required")
        url = CustomerEndpoint.DELETE_TAG.format(customer_id=customer_id)
        return self._request("DELETE", url, params={"tag": tag})

    def assign_customer(
        self,
        customer_id: str,
        assignee_id: Optional[str] = None,
        override: Optional[bool] = None,
    ) -> StatusResponse:
        """
        Assign a customer to an agent or team.

        Parameters
        ----------
        customer_id
            ID of the customer.
        assignee_id
            ID of the agent / team.
        override
            Force assignment. Default is False and skips assignment if the
            customer is already assigned.
        """
        if not customer_id:
            raise ValueError("Customer ID is required")
        url = CustomerEndpoint.ASSIGN_CUSTOMER.format(customer_id=customer_id)
        payload = self._clean(
            {
                "id": customer_id,
                "assigneeId": assignee_id,
                "override": override,
            }
        )
        return self._request("POST", url, json=payload)
