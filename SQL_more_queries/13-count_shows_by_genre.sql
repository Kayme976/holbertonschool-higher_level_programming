-- Import the database dump from hbtn_0d_tvshows same as 12-no_genre.sql
SELECT tv_genres.genre AS genre,
       COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
