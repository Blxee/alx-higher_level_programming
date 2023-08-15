-- Temperatures #1
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month in ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
