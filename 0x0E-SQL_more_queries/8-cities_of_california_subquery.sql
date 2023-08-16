-- Cities of California
SELECT id, name
FROM cities
WHERE (SELECT name FROM states WHERE id = state_id) = 'California'
ORDER BY id;
