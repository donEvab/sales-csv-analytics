import csv
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/orders.csv")


def extract_orders():
    with RAW_DATA_PATH.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    orders = extract_orders()
    print(f"Loaded {len(orders)} orders")
    print(orders[0:3])