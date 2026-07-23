def create_products(client):

    template_ids = []

    for i in range(1, 6):

        product_id = client.execute(
            "product.template",
            "create",
            [
                {
                    "name":
                        f"SYNC_TEST Product {i}",

                    "default_code":
                        f"SYNC_TEST-{i}",

                    "list_price":
                        100 * i,

                    "type":
                        "consu",
                }
            ],
        )

        template_ids.append(product_id)

    variants = []

    for template_id in template_ids:

        result = client.execute(
            "product.product",
            "search_read",
            [
                [
                    (
                        "product_tmpl_id",
                        "=",
                        template_id,
                    )
                ]
            ],
            {
                "fields": [
                    "id"
                ],
                "limit": 1,
            },
        )

        variants.append(
            result[0]["id"]
        )

    print(
        f"Created products: {len(variants)}"
    )

    return variants