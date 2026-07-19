# Customer resource - customers, properties, tags, assignment
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

zoko = ZokoClient(api_key=os.environ["ZOKO_API_KEY"])

CUSTOMER_ID = "3c90c3cc-0d44-4b50-8888-8dd25736052a"
PROPERTY_ID = "aa11bb22-0d44-4b50-8888-8dd25736052a"


def main():
    # get_customers -> {"currentPage": 1, "totalCustomers": N, "customers": [...]}
    page = zoko.customer.get_customers(channel="whatsapp", page_size=10)
    print(page)

    # get_customer -> {"id": ..., "name": ..., "channels": [...], "assignment": {...}}
    customer = zoko.customer.get_customer(CUSTOMER_ID)
    print(customer)

    # delete_messages (customer's messages, Zoko DB only) -> {"status": "204", ...}
    zoko.customer.delete_messages(CUSTOMER_ID)

    # --- Properties ---
    # list_properties -> [{"id": ..., "type": ..., "title": ..., ...}, ...]
    zoko.customer.list_properties(CUSTOMER_ID)

    # create_property -> {"status": "204", "message": ..., "details": ...}
    zoko.customer.create_property(
        CUSTOMER_ID, type="text", title="Plan", description="Pro", priority=1
    )

    # get_property -> {"id": ..., "type": ..., "title": ..., ...}
    zoko.customer.get_property(CUSTOMER_ID, PROPERTY_ID)

    # update_property -> {"id": ..., "title": "Enterprise", ...}
    zoko.customer.update_property(CUSTOMER_ID, PROPERTY_ID, title="Enterprise")

    # delete_property -> {"status": "204", ...}
    zoko.customer.delete_property(CUSTOMER_ID, PROPERTY_ID)

    # --- Tags ---
    # list_tags -> {"entityId": ..., "entityType": "customer", "tags": [...]}
    zoko.customer.list_tags(CUSTOMER_ID)

    # add_tag -> [{"status": "200", "message": "tag added", ...}]
    zoko.customer.add_tag(CUSTOMER_ID, "vip")

    # update_tags (replaces the whole list) -> [{"status": "200", ...}]
    zoko.customer.update_tags(CUSTOMER_ID, ["vip", "priority"])

    # delete_tag -> [{"status": "204", ...}]
    zoko.customer.delete_tag(CUSTOMER_ID, "vip")

    # --- Assignment ---
    # assign_customer -> {"status": "200", "message": "customer assigned", ...}
    zoko.customer.assign_customer(CUSTOMER_ID, assignee_id="agent-id", override=True)


if __name__ == "__main__":
    main()
