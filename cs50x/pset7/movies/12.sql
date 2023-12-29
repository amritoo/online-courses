SELECT title FROM movies
WHERE id IN
(
    SELECT movie_id from stars
    WHERE person_id = (SELECT id FROM people WHERE name = "Johnny Depp")
)

INTERSECT

SELECT title FROM movies
WHERE id IN
(
    SELECT movie_id from stars
    WHERE person_id = (SELECT id FROM people WHERE name = "Helena Bonham Carter")
);