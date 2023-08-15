-- This query retrieves scores and names from 'second_table' where  name is not null,
-- and orders the results in descending score
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
