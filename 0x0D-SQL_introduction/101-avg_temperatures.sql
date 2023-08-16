-- Query to display average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS average_temperature
-- Replace with the actual table name
FROM your_table_name
GROUP BY city
ORDER BY average_temperature DESC;
