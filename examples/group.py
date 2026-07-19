# Group resource - WhatsApp group management
#
# The group id used below is the internal UUID returned as `_id` by
# create_group, NOT Meta's group_id.
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])

GROUP_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


def main():
    # create_group -> {"_id": ..., "subject": ..., "status": "pending"|"complete", ...}
    group = zoko.group.create_group(subject="VIP Customers", description="Top buyers")
    print(group)

    # get_groups -> [{"id": ..., "subject": ..., "activeParticipantCount": N}, ...]
    zoko.group.get_groups()

    # get_group -> {"_id": ..., "subject": ..., "participants": [...], ...}
    zoko.group.get_group(GROUP_ID)

    # update_settings -> {"status": ..., "message": ...}
    zoko.group.update_settings(GROUP_ID, subject="VIP Members", description="Updated")

    # --- Members ---
    # invite_members -> {"sent": [...], "skipped": [...], "failed": [...]}
    zoko.group.invite_members(GROUP_ID, ["919998880000", "919998880001"])

    # remove_participants -> {"status": ..., "message": ...}
    zoko.group.remove_participants(GROUP_ID, ["919998880001"])

    # --- Invite link ---
    # get_invite_link -> {"invite_link": ...}
    zoko.group.get_invite_link(GROUP_ID)

    # reset_invite_link -> {"invite_link": ...}  (revokes old, returns new)
    zoko.group.reset_invite_link(GROUP_ID)

    # --- Join requests ---
    # get_join_requests -> {"count": N, "data": [...]}
    zoko.group.get_join_requests(GROUP_ID)

    # handle_join_requests (action: "approve" | "reject") -> {"status": ..., "message": ...}
    zoko.group.handle_join_requests(GROUP_ID, "approve", ["join-request-id"])

    # set_auto_approval -> {"status": ..., "message": ...}
    zoko.group.set_auto_approval(GROUP_ID, True)

    # --- Invitation template ---
    # get_invitation_template -> {"invitation_template_id": ..., "template_args": {...}}
    zoko.group.get_invitation_template(GROUP_ID)

    # set_invitation_template -> {"status": ..., "message": ...}
    zoko.group.set_invitation_template(GROUP_ID, invitation_template_id="invite_01")

    # delete_group (exit and delete) -> {"status": ..., "message": ...}
    zoko.group.delete_group(GROUP_ID)


if __name__ == "__main__":
    main()
