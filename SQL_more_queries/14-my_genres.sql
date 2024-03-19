-- Import the database dump from hbtn_0d_tvshows same as 13-count_shows_by_genre.sql
SELECT genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;