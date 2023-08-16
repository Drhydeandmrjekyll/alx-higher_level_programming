-- Retrieves TV show titles and their corresponding genre IDs through a LEFT JOIN between 'tv_shows' and 'tv_show_genres',
-- filtering for rows where there is no associated genre (NULL genre_id).
-- Results are ordered in ascending order of show title and genre ID.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
