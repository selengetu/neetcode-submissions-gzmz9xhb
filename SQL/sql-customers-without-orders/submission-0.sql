-- Write your query below
SELECT name FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
where o.customer_id is null