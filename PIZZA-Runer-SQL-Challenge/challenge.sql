-- INVESTIGATING THE DATA

-- A. Pizza Metrics
-- 1. How many pizzas were ordered?
SELECT COUNT(DISTINCT order_id) AS total_pizzas_ordered
FROM customer_orders;
--2. How many unique customer orders were made?
SELECT COUNT(DISTINCT customer_id) AS total_pizzas_ordered
FROM customer_orders;
--3. How many successful orders were delivered by each runner?

SELECT
  r.runner_id,
  COUNT(ro.order_id) AS successful_orders_delivered
FROM
  runners r
JOIN
  runner_orders ro ON r.runner_id = ro.runner_id
WHERE
  ro.cancellation IS NULL
GROUP BY
  r.runner_id
 ORDER BY runner_id ;
--4. How many of each type of pizza was delivered?

SELECT pn.pizza_name,
	COUNT(co.order_id)	total_delivered
FROM pizza_names pn 
JOIN customer_orders co 
ON  pn.pizza_id = co.pizza_id
JOIN runner_orders ro 
ON co.order_id = ro.order_id 
WHERE ro.cancellation IS NULL
GROUP BY pn.pizza_name 
;