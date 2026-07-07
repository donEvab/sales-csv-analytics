SELECT
    product,
    category,
    sum(quantity) as total_quantity_sold,
    sum(total_price) as total_revenue,
FROM orders
GROUP BY product, category
ORDER BY total_revenue DESC;