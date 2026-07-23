PREFIX = "SYNC_TEST"


def cleanup_contacts(client):

    ids = client.execute(
        "res.partner",
        "search",
        [
            [
                (
                    "email",
                    "ilike",
                    "sync_test%"
                )
            ]
        ],
    )

    if ids:
        client.execute(
            "res.partner",
            "unlink",
            [ids],
        )

    print(
        f"Deleted contacts: {len(ids)}"
    )


def cleanup_products(client):

    ids = client.execute(
        "product.template",
        "search",
        [
            [
                (
                    "default_code",
                    "ilike",
                    "SYNC_TEST%"
                )
            ]
        ],
    )

    if ids:
        client.execute(
            "product.template",
            "unlink",
            [ids],
        )

    print(
        f"Deleted products: {len(ids)}"
    )


def cleanup_orders(client):

    ids = client.execute(
        "sale.order",
        "search",
        [
            [
                (
                    "partner_id.name",
                    "ilike",
                    PREFIX
                )
            ]
        ],
    )

    if ids:
        client.execute(
            "sale.order",
            "unlink",
            [ids],
        )

    print(
        f"Deleted orders: {len(ids)}"
    )


def cleanup(client):

    cleanup_orders(client)
    cleanup_products(client)
    cleanup_contacts(client)