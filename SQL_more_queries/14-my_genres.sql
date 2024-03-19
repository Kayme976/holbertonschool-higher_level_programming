-- Import the database dump from hbtn_0d_tvshows same as 13-count_shows_by_genre.sql
SELECT g.name
    FROM (tv_shows s JOIN tv_show_genres sg ON s.id = sg.show_id)
    JOIN tv_genres g ON sg.genre_id = g.id
   WHERE s.title = "Dexter"
ORDER BY g.name ASC;