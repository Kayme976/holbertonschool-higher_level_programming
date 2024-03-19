-- Import the database dump from hbtn_0d_tvshows same as 13-count_shows_by_genre.sql
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;