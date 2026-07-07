import csv
import sqlite3
from pathlib import Path


DATABASE_PATH = Path("sales_analytics.db")
SQL_DIR = Path("sql")
REPORTS_DIR = Path("reports")


REPORT_QUERIES = {
    "revenue_summary": SQL_DIR / "revenue_summary.sql",
    "top_products": SQL_DIR / "top_products.sql",
    "customer_summary": SQL_DIR / "customer_summary.sql",
    "monthly_revenue": SQL_DIR / "monthly_revenue.sql",
}


def read_sql_file(sql_path):
    with sql_path.open(mode="r", encoding="utf-8") as file:
        return file.read()


def export_query_to_csv(connection, query_name, sql_path):
    query = read_sql_file(sql_path)
    cursor = connection.execute(query)

    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    output_path = REPORTS_DIR / f"{query_name}.csv"

    with output_path.open(mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        writer.writerows(rows)

    print(f"Exported {output_path}")


def export_reports():
    REPORTS_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        for query_name, sql_path in REPORT_QUERIES.items():
            export_query_to_csv(connection, query_name, sql_path)


if __name__ == "__main__":
    export_reports()