-- Retrieves TV show titles and associated genre IDs through a LEFT JOIN between 'tv_shows' and 'tv_show_genres' tables,
-- using 'id' and 'show_id' columns. Results are ordered by show title and genre ID.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
