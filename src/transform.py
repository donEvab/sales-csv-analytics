from datetime import datetime

def transform_date(raw_orders):
    clean_orders = []

    for order in raw_orders:
        quantity = int(order["quantity"])
        unit_price = int(order["unit_price"])

        clean_order.append({
            "order_id": int(order["order_id"]),
            "order_date": datetime.strptime(order["order_date"], "%Y-%m-%d").date().isoformat(),
            "customer_id": int(order["customer_id"]),
            "product": order["product"],
            "category": order["category"],
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": quantity * unit_price
        })
    
    return clean_orders
