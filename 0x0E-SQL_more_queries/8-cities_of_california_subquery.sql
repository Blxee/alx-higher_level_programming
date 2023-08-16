-- Cities of California
SELECT *
FROM cities
WHERE (SELECT name FROM states WHERE id = state_id) = 'California'
ORDER BY id;
