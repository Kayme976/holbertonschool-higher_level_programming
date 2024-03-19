-- Import the database dump from hbtn_0d_tvshows same as 12-no_genre.sql
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY COUNT(tv_show_genres.show_id) DESC;
