SELECT
    count(*) as total_orders,
    sum(quantity) as total_items_sold,
    sum(total_price) as total_revenue,
    round(avg(total_price), 2) as average_order_value
FROM orders;