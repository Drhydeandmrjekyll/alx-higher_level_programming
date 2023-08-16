-- Query to find maximum temperature by state
-- Select 'state' column and calculate  maximum temperature as 'max_temp'
-- Group the results by state
-- Order the results by state in ascending order
SELECT state,
       MAX(value) as max_temp
  FROM temperatures
GROUP BY state
ORDER BY state;
