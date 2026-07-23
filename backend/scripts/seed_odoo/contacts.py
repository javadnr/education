def create_contacts(client):

    ids = []

    for i in range(1, 6):

        partner_id = client.execute(
            "res.partner",
            "create",
            [
                {
                    "name":
                        f"SYNC_TEST Customer {i}",

                    "email":
                        f"sync_test{i}@example.com",

                    "phone":
                        f"021111111{i}",

                    "mobile":
                        f"091200000{i}",
                }
            ],
        )

        ids.append(partner_id)

    print(
        f"Created contacts: {len(ids)}"
    )

    return ids