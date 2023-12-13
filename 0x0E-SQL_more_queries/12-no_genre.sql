-- 12-no_genre.sql
SELECT DISTINCT ts.title, tsg.genre_id
FROM tv_shows AS ts
    LEFT JOIN tv_show_genres As tsg
    ON ts.id = tsg.show_id
    WHERE tsg.genre_id IS NOT NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;
