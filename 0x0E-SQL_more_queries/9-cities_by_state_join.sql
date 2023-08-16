-- Cities by States
SELECT c.id, c.name, s.name
FROM cities AS INNER JOIN states
ORDER BY c.id;
