# Sales CSV Analytics

A basic data engineering project that processes raw sales order data from CSV, loads it into a SQLite database, runs SQL analytics, and exports business reports as CSV files.

## Project Goal

The goal of this project is to practice the basic flow of a data engineering pipeline:

```text
Raw CSV -> Extract -> Transform -> Load -> SQL Analytics -> Report CSV
```

This project focuses on building a clear and reproducible workflow from raw data to analytical output.

## Data Source

The raw data is stored in:

```text
data/raw/orders.csv
```

The dataset contains sample sales orders with these columns:

- `order_id`
- `order_date`
- `customer_id`
- `customer_name`
- `product`
- `category`
- `quantity`
- `unit_price`

## Project Structure

```text
sales-csv-analytics/
  data/
    raw/
      orders.csv
    processed/
  reports/
  sql/
    revenue_summary.sql
    top_products.sql
    customer_summary.sql
    monthly_revenue.sql
  src/
    extract.py
    transform.py
    load.py
    pipeline.py
    analytics.py
  README.md
  requirements.txt
```

## Pipeline Flow

### 1. Extract

`src/extract.py` reads raw sales data from `data/raw/orders.csv`.

### 2. Transform

`src/transform.py` converts raw CSV values into cleaner data types and creates a new `total_price` field.

Example:

```text
quantity * unit_price = total_price
```

### 3. Load

`src/load.py` creates a SQLite database and loads the transformed data into an `orders` table.

Database output:

```text
sales_analytics.db
```

### 4. Analytics

SQL queries inside the `sql/` folder are used to answer business questions:

- How much total revenue was generated?
- Which products generated the most revenue?
- Which customers spent the most?
- How much revenue was generated per month?

### 5. Export Reports

`src/analytics.py` runs the SQL queries and exports the results into CSV files inside the `reports/` folder.

Generated reports:

```text
reports/revenue_summary.csv
reports/top_products.csv
reports/customer_summary.csv
reports/monthly_revenue.csv
```

## How To Run

Run the full ETL pipeline:

```bash
python src/pipeline.py
```

Then export the analytics reports:

```bash
python src/analytics.py
```

## Expected Output

After running the pipeline:

```text
Loaded 5 orders into sales_analytics.db
```

After exporting reports:

```text
Exported reports/revenue_summary.csv
Exported reports/top_products.csv
Exported reports/customer_summary.csv
Exported reports/monthly_revenue.csv
```

## Tools Used

- Python
- SQLite
- SQL
- CSV

## What I Learned

From this project, I learned how to:

- Read raw CSV data using Python
- Transform raw text values into clean data types
- Load structured data into a SQLite database
- Write SQL queries for business analytics
- Export query results into report files
- Organize a basic data engineering project structure

## Next Improvement

Possible improvements for this project:

- Add more sample data
- Add data validation for missing values
- Add automated tests
- Create charts from the reports
- Build a simple dashboard using Streamlit