-- Retrieves IDs and names of cities located in the state of California,
-- using a subquery to find corresponding state ID, and orders the results by ID.
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
