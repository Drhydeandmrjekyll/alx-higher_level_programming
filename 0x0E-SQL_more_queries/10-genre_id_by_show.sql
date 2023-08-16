-- Retrieves TV show titles and corresponding genre IDs by joining 'tv_shows' and 'tv_show_genres' tables
-- based on matching 'id' and 'show_id' columns. Results are ordered by show title and genre ID.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
