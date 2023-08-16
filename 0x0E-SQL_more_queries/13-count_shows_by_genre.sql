-- Counts TV shows in each genre by joining 'tv_genres' and 'tv_show_genres',grouping by genre and sorting by show count.
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
