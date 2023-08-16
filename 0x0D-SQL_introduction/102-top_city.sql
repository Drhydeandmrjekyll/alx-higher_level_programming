-- Query to calculate average temperature for cities in July and August
-- Select 'city' column and calculate average temperature as 'avg_temp'
-- Filter rows for the months of July (7) or August (8)
-- Group the results by city
-- Order the results in descending order based on the average temperature
-- Limit the output to the top 3 cities
SELECT city,
       AVG(value) AS avg_temp
  FROM temperatures
 WHERE month = 7
    OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
   LIMIT 3;
