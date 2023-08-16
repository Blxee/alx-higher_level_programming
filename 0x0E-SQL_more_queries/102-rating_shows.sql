-- Rotten tomatoes
SELECT
  tv_shows.title,
  SUM(tv_show_rating.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_rating
ON tv_shows.id = tv_show_rating.show_id
GROUP BY tv_shows.title
ORDER BY rating;
