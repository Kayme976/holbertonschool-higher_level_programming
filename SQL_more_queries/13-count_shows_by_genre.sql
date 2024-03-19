-- Import the database dump from hbtn_0d_tvshows same as 12-no_genre.sql
SELECT g.name AS genre, COUNT(sg.genre_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
