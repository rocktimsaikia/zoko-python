# Roots
ROOT = "https://chat.zoko.io"
ZOKO_API_V2 = ROOT + "/v2"

# Resources:
ACCOUNT = ZOKO_API_V2 + "/account"
MESSAGE = ZOKO_API_V2 + "/message"
CUSTOMER = ZOKO_API_V2 + "/customer"
AGENT = ZOKO_API_V2 + "/agent"
WEBHOOK = ZOKO_API_V2 + "/webhook"
GROUP = ZOKO_API_V2 + "/channels/whatsapp/cloud/group"


class AccountEndpoint(object):
    # Account
    TEMPLATES = ACCOUNT + "/templates"


class MessageEndpoint(object):
    # Message
    SEND = MESSAGE
    GET = MESSAGE + "/{message_id}"
    DELETE = MESSAGE + "/{message_id}"
    HISTORY = MESSAGE + "/{message_id}/history"
    BATCH_DELETE = MESSAGE + "/batch"


class CustomerEndpoint(object):
    # Customer
    LIST = CUSTOMER
    GET = CUSTOMER + "/{customer_id}"
    DELETE = CUSTOMER + "/{customer_id}/messages"
    LIST_PROPERTIES = CUSTOMER + "/{customer_id}/properties"
    CREATE_PROPERTY = CUSTOMER + "/{customer_id}/properties"
    GET_PROPERTY = CUSTOMER + "/{customer_id}/properties/{property_id}"
    UPDATE_PROPERTY = CUSTOMER + "/{customer_id}/properties/{property_id}"
    DELETE_PROPERTY = CUSTOMER + "/{customer_id}/properties/{property_id}"
    LIST_TAGS = CUSTOMER + "/{customer_id}/tags"
    UPDATE_TAGS = CUSTOMER + "/{customer_id}/tags"  # bulk
    ADD_TAG = CUSTOMER + "/{customer_id}/tags"
    DELETE_TAG = CUSTOMER + "/{customer_id}/tags"
    ASSIGN_CUSTOMER = CUSTOMER + "/{customer_id}/assign"


class AgentEndpoint(object):
    # Agent
    GET = AGENT + "/{agent_id}"
    UPDATE = AGENT + "/{agent_id}"
    LIST_AGENTS = AGENT + "/agents"
    LIST_TEAMS = AGENT + "/teams"


class WebhookEndpoint(object):
    LIST = WEBHOOK
    CREATE = WEBHOOK
    GET = WEBHOOK + "/{webhook_id}"
    UPDATE = WEBHOOK + "/{webhook_id}"
    DELETE = WEBHOOK + "/{webhook_id}"


class GroupEndpoint(object):
    CREATE = GROUP
    LIST = GROUP
    GET = GROUP + "/{group_id}"
    UPDATE_SETTINGS = GROUP + "/{group_id}/settings"
    DELETE = GROUP + "/{group_id}/delete"
    INVITE = GROUP + "/{group_id}/invitations"
    REMOVE_PARTICIPANTS = GROUP + "/{group_id}/remove-participants"
    INVITE_LINK = GROUP + "/{group_id}/invite-link"
    JOIN_REQUESTS = GROUP + "/{group_id}/join-requests"
    HANDLE_JOIN_REQUESTS = GROUP + "/{group_id}/join-requests/{action}"
    AUTO_APPROVAL = GROUP + "/{group_id}/auto-approval"
    INVITATION_TEMPLATE = GROUP + "/{group_id}/invitation-template"
