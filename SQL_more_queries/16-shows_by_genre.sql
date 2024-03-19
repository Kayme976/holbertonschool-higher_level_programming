-- Import the database dump from hbtn_0d_tvshows same as 15-comedy_only.sql
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN show_genres ON tv_shows.id = show_genres.show_id
LEFT JOIN tv_genres ON show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;