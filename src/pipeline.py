from extract import extract_orders
from transform import transform_orders
from load import load_orders


def run_pipeline():
    raw_orders = extract_orders()
    clean_orders = transform_orders(raw_orders)
    load_orders(clean_orders)


if __name__ == "__main__":
    run_pipeline()