import random


def create_sale_orders(
    client,
    customer_ids,
    product_ids,
):

    order_ids = []

    for i in range(1, 4):

        lines = []

        for _ in range(2):

            lines.append(
                (
                    0,
                    0,
                    {
                        "product_id":
                            random.choice(
                                product_ids
                            ),

                        "product_uom_qty":
                            random.randint(
                                1,
                                5
                            ),
                    },
                )
            )

        order_id = client.execute(
            "sale.order",
            "create",
            [
                {
                    "partner_id":
                        random.choice(
                            customer_ids
                        ),

                    "order_line":
                        lines,
                }
            ],
        )

        order_ids.append(order_id)

    print(
        f"Created sale orders: {len(order_ids)}"
    )

    return order_ids