-- Import the database dump from hbtn_0d_tvshows
SELECT s.title, g.genre_id
FROM tv_show s
INNER JOIN tv_show_genres g
ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id ASC;