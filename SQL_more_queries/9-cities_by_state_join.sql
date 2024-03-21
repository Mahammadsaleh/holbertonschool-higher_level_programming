-- Cities by States
SELECT cities.id, cities.name, states.name FROM cities
JOIN sates ON cities.state_id = states.id
ORDER BY cities.id ASC;
