from typing import List, Optional

from zoko.constants.endpoint import GroupEndpoint
from zoko.resources.base import Resource
from zoko.types.common import JoinRequestAction


class Group(Resource):
    """
    WhatsApp Cloud group management.

    Note: the group identifier used across these methods is the internal UUID
    returned as ``_id`` by :meth:`create_group`, not the Meta ``group_id``.
    """

    def create_group(
        self,
        subject: str,
        description: Optional[str] = None,
        agent_id: Optional[str] = None,
    ) -> dict:
        """
        Create a new WhatsApp group.

        The response may be HTTP 202 (async, pending Meta webhook) or HTTP 200
        (completed synchronously).

        Parameters
        ----------
        subject
            Group name/subject (<= 128 characters).
        description
            Group description (<= 2048 characters).
        agent_id
            ID of the agent creating the group.
        """
        if not subject:
            raise ValueError("Group subject is required")
        payload = self._clean(
            {"subject": subject, "description": description, "agent_id": agent_id}
        )
        return self._request("POST", GroupEndpoint.CREATE, json=payload)

    def get_groups(self) -> List[dict]:
        """Retrieve all active WhatsApp groups for the store."""
        return self._request("GET", GroupEndpoint.LIST)

    def get_group(self, group_id: str) -> dict:
        """Retrieve details of a group, including its participants."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.GET.format(group_id=group_id)
        return self._request("GET", url)

    def update_settings(
        self,
        group_id: str,
        subject: Optional[str] = None,
        description: Optional[str] = None,
        photo_url: Optional[str] = None,
        messaging_settings: Optional[str] = None,
        agent_email: Optional[str] = None,
    ) -> dict:
        """
        Update group subject, description, messaging settings, or photo.

        Parameters
        ----------
        photo_url
            Publicly reachable HTTPS URL of the new group photo. Must be JPEG,
            <= 5MB, square, and at least 192x192 px.
        """
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.UPDATE_SETTINGS.format(group_id=group_id)
        payload = self._clean(
            {
                "subject": subject,
                "description": description,
                "photo_url": photo_url,
                "messaging_settings": messaging_settings,
                "agent_email": agent_email,
            }
        )
        return self._request("PUT", url, json=payload)

    def delete_group(self, group_id: str) -> dict:
        """Exit and delete a WhatsApp group."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.DELETE.format(group_id=group_id)
        return self._request("POST", url)

    def invite_members(self, group_id: str, phone_numbers: List[str]) -> dict:
        """
        Send template invitations to phone numbers to join the group.

        Numbers already joined, left, removed, or with a pending invitation are
        skipped.
        """
        if not group_id:
            raise ValueError("Group ID is required")
        if not phone_numbers:
            raise ValueError("At least one phone number is required")
        url = GroupEndpoint.INVITE.format(group_id=group_id)
        return self._request("POST", url, json={"phone_numbers": phone_numbers})

    def remove_participants(
        self,
        group_id: str,
        participants: List[str],
        agent_email: Optional[str] = None,
    ) -> dict:
        """
        Remove specific participants from the group.

        Parameters
        ----------
        participants
            WhatsApp IDs of participants to remove.
        agent_email
            Email of the agent performing the action.
        """
        if not group_id:
            raise ValueError("Group ID is required")
        if not participants:
            raise ValueError("At least one participant is required")
        url = GroupEndpoint.REMOVE_PARTICIPANTS.format(group_id=group_id)
        payload = self._clean(
            {"participants": participants, "agent_email": agent_email}
        )
        return self._request("POST", url, json=payload)

    def get_invite_link(self, group_id: str) -> dict:
        """Retrieve the current invite link for the group."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.INVITE_LINK.format(group_id=group_id)
        return self._request("GET", url)

    def reset_invite_link(self, group_id: str) -> dict:
        """Revoke the current invite link and generate a new one."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.INVITE_LINK.format(group_id=group_id)
        return self._request("PUT", url)

    def get_join_requests(self, group_id: str) -> dict:
        """Retrieve pending join requests for the group."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.JOIN_REQUESTS.format(group_id=group_id)
        return self._request("GET", url)

    def handle_join_requests(
        self,
        group_id: str,
        action: JoinRequestAction,
        join_requests: List[str],
    ) -> dict:
        """
        Approve or reject pending join requests for the group.

        Parameters
        ----------
        action
            "approve" or "reject".
        join_requests
            List of join request IDs to act on.
        """
        if not group_id:
            raise ValueError("Group ID is required")
        if action not in ("approve", "reject"):
            raise ValueError("Action must be 'approve' or 'reject'")
        if not join_requests:
            raise ValueError("At least one join request ID is required")
        url = GroupEndpoint.HANDLE_JOIN_REQUESTS.format(
            group_id=group_id, action=action
        )
        return self._request("POST", url, json={"join_requests": join_requests})

    def set_auto_approval(self, group_id: str, auto_approval: bool) -> dict:
        """Enable or disable automatic approval of join requests."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.AUTO_APPROVAL.format(group_id=group_id)
        return self._request("PUT", url, json={"auto_approval": auto_approval})

    def get_invitation_template(self, group_id: str) -> dict:
        """Retrieve the invitation template ID and args configured for the group."""
        if not group_id:
            raise ValueError("Group ID is required")
        url = GroupEndpoint.INVITATION_TEMPLATE.format(group_id=group_id)
        return self._request("GET", url)

    def set_invitation_template(
        self,
        group_id: str,
        invitation_template_id: str,
        template_args: Optional[dict] = None,
    ) -> dict:
        """
        Configure the invitation template used when inviting members.

        Template variables: {{brand.whatsapp_display_name}} (store name),
        {{group.invite_link}} (invite link).
        """
        if not group_id:
            raise ValueError("Group ID is required")
        if not invitation_template_id:
            raise ValueError("Invitation template ID is required")
        url = GroupEndpoint.INVITATION_TEMPLATE.format(group_id=group_id)
        payload = self._clean(
            {
                "invitation_template_id": invitation_template_id,
                "template_args": template_args,
            }
        )
        return self._request("PUT", url, json=payload)
