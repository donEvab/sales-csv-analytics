SELECT
    customer_id,
    customer_name,
    count(*) as total_orders,
    sum(quantity) as total_items_bought,
    sum(total_price) as total_spent
FROM orders
GROUP BY customer_id, customer_name
ORDER BY total_spent DESC;
