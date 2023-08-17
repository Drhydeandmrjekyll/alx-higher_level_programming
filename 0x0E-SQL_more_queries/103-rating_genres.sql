-- Retrieves the sum of TV show ratings for each genre by performing INNER JOINs between 'tv_genres', 'tv_show_genres',
-- and 'tv_show_ratings' tables. Results are grouped by genre name and ordered in descending order of total rating.
SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
