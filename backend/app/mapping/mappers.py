def map_contact(raw: dict) -> dict:
    return {
        "name": raw.get("name") or "",
        "email": raw.get("email") or None,
        "phone": raw.get("phone") or None,
        "mobile": raw.get("mobile") or None,
    }


def map_sale_order(raw: dict, customer_internal_id: int) -> dict:
    return {
        "order_number": raw.get("name"),
        "customer_id": customer_internal_id,
        "order_date": raw.get("date_order"),
        "state": raw.get("state"),
        "total_amount": raw.get("amount_total"),
    }