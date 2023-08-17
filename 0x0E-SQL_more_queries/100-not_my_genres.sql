-- Not my genre
SELECT DISTINCT name
FROM tv_genres
WHERE id NOT IN (
  SELECT DISTINCT tv_genres.id
  FROM tv_genres
  LEFT JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
  INNER JOIN tv_shows
  ON tv_show_genres.show_id = tv_shows.id
  WHERE tv_genres.name = 'Dexter'
)
ORDER BY name;
