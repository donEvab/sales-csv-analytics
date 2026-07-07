import sqlite3
from pathlib import Path


DATABASE_PATH = Path("sales_analytics.db")


def create_orders_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            customer_id TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            product TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price INTEGER NOT NULL,
            total_price INTEGER NOT NULL
        )
    """)


def load_orders(clean_orders):
    with sqlite3.connect(DATABASE_PATH) as connection:
        create_orders_table(connection)

        connection.execute("DELETE FROM orders")

        connection.executemany("""
            INSERT INTO orders (
                order_id,
                order_date,
                customer_id,
                customer_name,
                product,
                category,
                quantity,
                unit_price,
                total_price
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            (
                order["order_id"],
                order["order_date"],
                order["customer_id"],
                order["customer_name"],
                order["product"],
                order["category"],
                order["quantity"],
                order["unit_price"],
                order["total_price"],
            )
            for order in clean_orders
        ])

    print(f"Loaded {len(clean_orders)} orders into {DATABASE_PATH}")