# Roots
ROOT = "https://chat.zoko.io"
ZOKO_API_V2 = ROOT + "/v2"

# Resources:
ACCOUNT = ZOKO_API_V2 + "/account"
MESSAGE = ZOKO_API_V2 + "/message"
CUSTOMER = ZOKO_API_V2 + "/customer"
AGENT = ZOKO_API_V2 + "/agent"
WEBHOOK = ZOKO_API_V2 + "/webhook"


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
    LIST = AGENT + "/agents"
    GET = AGENT + "/{agent_id}"
    UPDATE = AGENT + "/{agent_id}"
    LIST_AGENTS = AGENT + "/teams"


class Webhook(object):
    LIST = WEBHOOK
    CREATE = WEBHOOK
    GET = WEBHOOK + "/{webhook_id}"
    UPDATE = WEBHOOK + "/{webhook_id}"
