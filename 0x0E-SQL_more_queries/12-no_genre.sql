-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT shows.title, genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
ON genres.show_id = id
WHERE genres.show_id is NULL
ORDER BY shows.title;

