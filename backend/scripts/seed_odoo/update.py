def update(client):

    update_contacts(client)
    update_products(client)
    update_sale_orders(client)
    update_sale_order_lines(client)


def update_contacts(client):

    contacts = client.execute(
        model="res.partner",
        method="search_read",
        args=[[]],
        kwargs={
            "fields": ["id", "name"],
        },
    )

    for contact in contacts:
        client.execute(
            model="res.partner",
            method="write",
            args=[
                [contact["id"]],
                {
                    "phone": f"021-{contact['id']:04}",
                    "mobile": f"0912000{contact['id']:04}",
                },
            ],
        )

    print(f"Updated {len(contacts)} contacts")


def update_products(client):

    products = client.execute(
        model="product.template",
        method="search_read",
        args=[[]],
        kwargs={
            "fields": ["id", "list_price"],
        },
    )

    for product in products:
        client.execute(
            model="product.template",
            method="write",
            args=[
                [product["id"]],
                {
                    "list_price": product["list_price"] + 100,
                },
            ],
        )

    print(f"Updated {len(products)} products")


def update_sale_orders(client):

    orders = client.execute(
        model="sale.order",
        method="search_read",
        args=[[]],
        kwargs={
            "fields": ["id", "note"],
        },
    )

    for order in orders:
        client.execute(
            model="sale.order",
            method="write",
            args=[
                [order["id"]],
                {
                    "note": f"Updated order #{order['id']}",
                },
            ],
        )

    print(f"Updated {len(orders)} sale orders")


def update_sale_order_lines(client):

    lines = client.execute(
        model="sale.order.line",
        method="search_read",
        args=[[]],
        kwargs={
            "fields": ["id", "price_unit"],
        },
    )

    for line in lines:
        client.execute(
            model="sale.order.line",
            method="write",
            args=[
                [line["id"]],
                {
                    "price_unit": line["price_unit"] + 10,
                },
            ],
        )

    print(f"Updated {len(lines)} sale order lines")