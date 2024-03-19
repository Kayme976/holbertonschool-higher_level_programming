-- Import the database dump from hbtn_0d_tvshows same as 15-comedy_only.sql
SELECT s.title, g.name
FROM (tv_shows s LEFT JOIN tv_show_genres sg ON s.id = sg.show_id)
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title, g.name ASC;