-- Retrieves titles and genre IDs of TV shows through a LEFT JOIN with 'tv_show_genres',
-- filtering out rows without corresponding genres. Results are sorted by title and genre ID.
SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;

