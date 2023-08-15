-- This query retrieves scores and counts number of occurrences for each score from 'second_table',
-- then orders the results by the count in descending order
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
