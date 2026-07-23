from client import OdooClient

from cleanup import cleanup
from contacts import create_contacts
from products import create_products
from sale_orders import create_sale_orders
from verify import verify
from update import update

from dotenv import load_dotenv

import os

load_dotenv()

def main():

    client = OdooClient(
        url=os.getenv("ODOO_URL"),
        database=os.getenv("ODOO_DATABASE"),
        username=os.getenv("ODOO_USERNAME"),
        password=os.getenv("ODOO_PASSWORD"),
    )
    

    cleanup(client)

    customers = create_contacts(
        client
    )

    products = create_products(
        client
    )

    create_sale_orders(
        client,
        customers,
        products,
    )

    print("Odoo seed completed")


    update(client)

    print("Odoo data updated")

    verify(client)


if __name__ == "__main__":
    main()