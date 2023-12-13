-- 11-genre_id_all_shows.sql
-- List all shows with at least one linked genre
SELECT DISTINCT ts.title, tsg.genre_id
FROM tv_shows AS ts
    LEFT JOIN tv_show_genres As tsg
    ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;
