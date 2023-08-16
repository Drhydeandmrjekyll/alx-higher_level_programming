-- Joins 'cities' and 'states' tables on state_id to get city and corresponding state names, ordered by city ID.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
