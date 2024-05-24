-- 1. Encuentra el título y la fecha de estreno de las películas que tienen "El" en su título
SELECT title, release_date
FROM movie
WHERE title LIKE '%El%';

-- 2. Encuentra el título y director de las películas estrenadas después de 2000
SELECT title, director
FROM  movie
WHERE EXTRACT(YEAR FROM release_date) > 2000;

-- 3. Encuentra el título y el director de las películas que fueron estrenadas antes de 1990 o después de 2010
SELECT title, director, EXTRACT(YEAR FROM release_date) as anio
FROM  movie
WHERE EXTRACT(YEAR FROM release_date) < 1990 OR EXTRACT(YEAR FROM release_date) > 2010;

-- 4. Encuentra todas las películas cuyo año de estreno sea 1994 o 1997
SELECT * FROM  movie 
WHERE EXTRACT(YEAR FROM release_date) IN (1994, 1997);

-- 5. Encuentra todas las películas junto con las críticas asociadas
SELECT m.title, r.reviewer_name, r.rating, r.comment
FROM  movie m
INNER JOIN  review r ON m.id_movie = r.id_movie;

-- 6. Encuentra todas las películas, incluso si no tienen críticas asociadas
SELECT m.title, COALESCE(r.reviewer_name, 'Sin críticas') AS reviewer_name, r.rating, r.comment
FROM  movie m
LEFT JOIN  review r ON m.id_movie = r.id_movie;

-- 7. Encuentra todas las críticas, incluso si no están asociadas a una película
SELECT r.reviewer_name, r.rating, r.comment, COALESCE(m.title, 'Sin película asociada') AS movie_title
FROM  review r
RIGHT JOIN  movie m ON r.id_movie = m.id_movie;

-- 8. Encuentra el título de la película, el nombre del crítico y su comentario para todas las críticas con una calificación de 4 o más
SELECT m.title, r.reviewer_name, r.comment
FROM  movie m
JOIN  review r ON m.id_movie = r.id_movie
WHERE r.rating >= 4;

-- 9. Encuentra el promedio de calificaciones por película, agregar numero de review, por último solo para películas con más de una crítica
SELECT m.title, AVG(r.rating) AS average_rating, COUNT(r.id_review) as number_reviews
FROM  movie m
JOIN  review r ON m.id_movie = r.id_movie
GROUP BY m.title
HAVING COUNT(r.id_review) > 1;

-- 10. Encuentra el nombre de los críticos y la cantidad de críticas que han realizado
SELECT r.reviewer_name, COUNT(r.id_review) AS num_reviews
FROM  review r
GROUP BY r.reviewer_name;

-- 11. Encuentra las películas junto con sus géneros
SELECT m.title, STRING_AGG(g.name, ', ') AS genre
FROM  movie m
INNER JOIN  movie_genre mg ON m.id_movie = mg.id_movie
INNER JOIN  genre g ON mg.id_genre = g.id_genre
GROUP BY m.title;

-- 12. Buscar el nombre de la película y el rating máximo y mínimo recibido
SELECT 
    m.title,
    MAX(r.rating) AS max_rating,
    MIN(r.rating) AS min_rating
FROM 
     movie m
LEFT JOIN 
     review r ON m.id_movie = r.id_movie
GROUP BY 
    m.title;
