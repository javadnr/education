PREFIX = "SYNC_TEST"


def verify_contacts(client):

    contacts = client.execute(
        "res.partner",
        "search_read",
        [
            [
                (
                    "email",
                    "ilike",
                    "sync_test%"
                )
            ]
        ],
        {
            "fields": [
                "id",
                "name",
                "email",
                "phone",
                "mobile",
            ]
        },
    )

    print("\nCONTACTS")
    print("-" * 50)

    for contact in contacts:
        print(contact)

    return len(contacts)


def verify_products(client):

    products = client.execute(
        "product.template",
        "search_read",
        [
            [
                (
                    "default_code",
                    "ilike",
                    "SYNC_TEST%"
                )
            ]
        ],
        {
            "fields": [
                "id",
                "name",
                "default_code",
                "list_price",
                "type",
            ]
        },
    )

    print("\nPRODUCTS")
    print("-" * 50)

    for product in products:
        print(product)

    return len(products)


def verify_orders(client):

    orders = client.execute(
        "sale.order",
        "search_read",
        [
            [
                (
                    "partner_id.name",
                    "ilike",
                    PREFIX
                )
            ]
        ],
        {
            "fields": [
                "id",
                "name",
                "partner_id",
                "date_order",
                "state",
                "amount_total",
            ]
        },
    )

    print("\nSALE ORDERS")
    print("-" * 50)

    for order in orders:
        print(order)

    return len(orders)


def verify_order_lines(client):

    lines = client.execute(
        "sale.order.line",
        "search_read",
        [
            [
                (
                    "order_id.partner_id.name",
                    "ilike",
                    PREFIX
                )
            ]
        ],
        {
            "fields": [
                "id",
                "order_id",
                "product_id",
                "product_uom_qty",
                "price_unit",
                "price_subtotal",
            ]
        },
    )

    print("\nSALE ORDER LINES")
    print("-" * 50)

    for line in lines:
        print(line)

    return len(lines)


def verify(client):

    contacts_count = verify_contacts(client)

    products_count = verify_products(client)

    orders_count = verify_orders(client)

    lines_count = verify_order_lines(client)


    print("\nSUMMARY")
    print("=" * 50)

    print(
        f"Contacts: {contacts_count}"
    )

    print(
        f"Products: {products_count}"
    )

    print(
        f"Sale Orders: {orders_count}"
    )

    print(
        f"Sale Order Lines: {lines_count}"
    )


    if (
        contacts_count >= 5
        and products_count >= 5
        and orders_count >= 3
        and lines_count > 0
    ):
        print(
            "\n✅ Odoo test data is valid"
        )

    else:
        print(
            "\n❌ Odoo test data is incomplete"
        )