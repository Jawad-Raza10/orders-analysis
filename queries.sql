-- (a) INNER JOIN
SELECT c.name, o.amount
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id;


-- (b) GROUP BY + SUM
SELECT c.name, SUM(o.amount) AS total_spent
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;


-- (c) GROUP BY + HAVING
SELECT c.city, AVG(o.amount) AS average_order
FROM customers AS c
INNER JOIN orders AS o
ON c.customer_id = o.customer_id
GROUP BY c.city
HAVING AVG(o.amount) > 5000;