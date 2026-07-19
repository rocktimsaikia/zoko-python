# List customers and tag the first one
import os

from dotenv import load_dotenv

from zoko import ZokoClient

load_dotenv()

ZOKO_API_KEY = os.environ["ZOKO_API_KEY"]


def main():
    zoko = ZokoClient(api_key=ZOKO_API_KEY)

    result = zoko.customer.get_customers(channel="whatsapp", page_size=10)
    print(f"Total customers: {result['totalCustomers']}")

    customers = result["customers"]
    if customers:
        customer_id = customers[0]["id"]
        zoko.customer.add_tag(customer_id, "vip")
        print(zoko.customer.list_tags(customer_id))


if __name__ == "__main__":
    main()
