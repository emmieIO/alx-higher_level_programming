-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name , state.name
FROM cities AS c
    INNER JOIN states AS s
    ON c.state_id = s.id
ORDER BY c.id ASC