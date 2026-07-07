SELECT
    strftime('%Y-%m', order_date) as sales_month,
    count(*) as total_orders,
    sum(total_price) as total_revenue
FROM orders
GROUP BY sales_month
ORDER BY sales_month;