CREATE SCHEMA `cac_movies_bd` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE `cac_movies_bd`.`genres` (
  `id_genre` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  PRIMARY KEY (`id_genre`));

ALTER TABLE `cac_movies_bd`.`genres` 
CHANGE COLUMN `name` `name` VARCHAR(20) NOT NULL ;


CREATE TABLE `cac_movies_bd`.`movies` (
  `id_movie` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `release_date` DATE NULL,
  `director` VARCHAR(50) NULL,
  PRIMARY KEY (`id_movie`));

Tengo la siguiente estructura de una tabla, necesito que me facilites 20 sentencias INSERT de acuerdo a los registros de movies que me diste, puedes hacer que una movie tenga hasta 3 reviews y otras ninguna. Tienen que estar en español
CREATE TABLE `cac_movies_bd`.`reviews` (
  `id_review` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NULL,
  `reviewer_name` VARCHAR(100) NULL,
  `comment` TEXT NULL,
  `rating` DECIMAL(4,2) NULL,
  PRIMARY KEY (`id_review`));

ALTER TABLE `cac_movies_bd`.`reviews` 
ADD INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE;
;
ALTER TABLE `cac_movies_bd`.`reviews` 
ADD CONSTRAINT `fk_movie`
  FOREIGN KEY (`id_movie`)
  REFERENCES `cac_movies_bd`.`movies` (`id_movie`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


CREATE TABLE `cac_movies_bd`.`movies_genres` (
  `id_movie_genre` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NOT NULL,
  `id_genre` INT NOT NULL,
  PRIMARY KEY (`id_movie_genre`),
  INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE,
  INDEX `fk_genre_idx` (`id_genre` ASC) VISIBLE,
  CONSTRAINT `fk_mg_movie`
    FOREIGN KEY (`id_movie`)
    REFERENCES `cac_movies_bd`.`movies` (`id_movie`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_mg_genre`
    FOREIGN KEY (`id_genre`)
    REFERENCES `cac_movies_bd`.`genres` (`id_genre`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

/* INSERTS */
INSERT INTO genres (name) VALUES ('Acción');
INSERT INTO genres (name) VALUES ('Comedia');
INSERT INTO genres (name) VALUES ('Drama');
INSERT INTO genres (name) VALUES ('Ciencia Ficción');
INSERT INTO genres (name) VALUES ('Romance');
INSERT INTO genres (name) VALUES ('Terror');
INSERT INTO genres (name) VALUES ('Aventura');
INSERT INTO genres (name) VALUES ('Animación');
INSERT INTO genres (name) VALUES ('Fantasía');
INSERT INTO genres (name) VALUES ('Documental');

INSERT INTO movies (title, release_date, director) VALUES ('El Señor de los Anillos: La Comunidad del Anillo', '2001-12-19', 'Peter Jackson');
INSERT INTO movies (title, release_date, director) VALUES ('Pulp Fiction', '1994-10-14', 'Quentin Tarantino');
INSERT INTO movies (title, release_date, director) VALUES ('Titanic', '1997-12-19', 'James Cameron');
INSERT INTO movies (title, release_date, director) VALUES ('Forrest Gump', '1994-07-06', 'Robert Zemeckis');
INSERT INTO movies (title, release_date, director) VALUES ('El Rey León', '1994-06-24', 'Roger Allers, Rob Minkoff');
INSERT INTO movies (title, release_date, director) VALUES ('El Padrino', '1972-03-24', 'Francis Ford Coppola');
INSERT INTO movies (title, release_date, director) VALUES ('Interestelar', '2014-11-07', 'Christopher Nolan');
INSERT INTO movies (title, release_date, director) VALUES ('Harry Potter y la piedra filosofal', '2001-11-30', 'Chris Columbus');
INSERT INTO movies (title, release_date, director) VALUES ('La La Land', '2016-12-09', 'Damien Chazelle');
INSERT INTO movies (title, release_date, director) VALUES ('El club de la lucha', '1999-10-15', 'David Fincher');


-- Asociación de "El Señor de los Anillos: La Comunidad del Anillo" con los géneros "Acción" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (1, 1), (1, 7);

-- Asociación de "Pulp Fiction" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (2, 3), (2, 8);

-- Asociación de "Titanic" con los géneros "Romance" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (3, 5), (3, 3);

-- Asociación de "Forrest Gump" con el género "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (4, 3);

-- Asociación de "El Rey León" con los géneros "Animación" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (5, 8), (5, 7);

-- Asociación de "El Padrino" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (6, 3), (6, 8);

-- Asociación de "Interestelar" con el género "Ciencia Ficción"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (7, 4);

-- Asociación de "Harry Potter y la piedra filosofal" con los géneros "Fantasía" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (8, 9), (8, 7);

-- Asociación de "La La Land" con los géneros "Musical" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (9, 10), (9, 3);

-- Asociación de "El club de la lucha" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (10, 3), (10, 8);

-- Críticas para "El Señor de los Anillos: La Comunidad del Anillo"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (1, 'María', 'Una gran película de aventuras.', 4.5);
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (1, 'Juan', 'El inicio de una gran saga.', 4.8);
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (1, 'Luis', 'Impresionante, ¡quiero más elfos!', 4.7);

-- Crítica para "Titanic"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (3, 'Ana', 'Una historia de amor inolvidable.', 4.2);
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (3, 'Carlos', 'Una experiencia cinematográfica épica.', 4.6);

-- Crítica para "Forrest Gump"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (4, 'Pedro', 'Una película que te llega al corazón.', 4.6);
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (4, 'Laura', 'Una película que te hace sentir muchas emociones.', 4.7);

-- Crítica para "El Padrino"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (6, 'Martín', 'Un clásico indiscutible del cine.', 4.9);

-- Crítica para "Interestelar"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (7, 'Elena', 'Una obra maestra del sci-fi.', 4.8);
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (7, 'Luisa', 'Un viaje emocionante a través del espacio.', 4.9);
-- Crítica para "Harry Potter y la piedra filosofal"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (8, 'Javier', 'El inicio de una gran saga.', 4.7);

-- Crítica para "La La Land"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (9, 'Lucía', 'Un musical moderno y encantador.', 4.4);

-- Crítica para "El club de la lucha"
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (10, 'Marta', 'Una película que te hace reflexionar.', 4.3);


EJEMPLOS DE CONSULTAS BASICAS
Encuentra el título y la fecha de estreno de las películas que tienen  "El" en su título:BINARY
SELECT title, release_date
FROM movies
WHERE title LIKE '%El%';

Encuentra el título y director de las peliculas estrenadas después de 2000:
SELECT title, director
FROM movies
WHERE YEAR(release_date) > 2000;

Encuentra el título y el director de las películas que fueron estrenadas antes de 1990 o después de 2010
SELECT title, director, YEAR(release_date) as anio
FROM movies
WHERE YEAR(release_date) < 1990 OR YEAR(release_date) > 2010;

Encuentra todas las películas cuyo año de estreno sea 1994 o 1997.
SELECT * FROM movies WHERE YEAR(release_date) IN (1994, 1997);


EJEMPLOS CON JOINS
1. INNER JOIN (Unión Interna):
Enunciado: Encuentra todas las películas junto con las críticas asociadas.
SELECT m.title, r.reviewer_name, r.rating, r.comment
FROM movies m
INNER JOIN reviews r ON m.id_movie = r.id_movie;

2. LEFT JOIN (Unión Izquierda):
Enunciado: Encuentra todas las películas, incluso si no tienen críticas asociadas.
SELECT m.title, COALESCE(r.reviewer_name, 'Sin críticas') AS reviewer_name, r.rating, r.comment
FROM movies m
LEFT JOIN reviews r ON m.id_movie = r.id_movie;

3. RIGHT JOIN (Unión Derecha):
Enunciado: Encuentra todas las críticas, incluso si no están asociadas a una película
SELECT r.reviewer_name, r.rating, r.comment, COALESCE(m.title, 'Sin película asociada') AS movie_title
FROM reviews r
RIGHT JOIN movies m ON r.id_movie = m.id_movie;

OTROS

1. Encuentra el título de la película, el nombre del crítico y su comentario para
todas las críticas con una calificación de 4 o más:
SELECT m.title, r.reviewer_name, r.comment
FROM movies m
JOIN reviews r ON m.id_movie = r.id_movie
WHERE r.rating >= 4;

2-Encuentra el promedio de calificaciones por película, agregar numero de reviews, por último solo para películas 
con más de una crítica:
SELECT m.title, AVG(r.rating) AS average_rating,  COUNT(r.id_review) as number_reviews
FROM movies m
JOIN reviews r ON m.id_movie = r.id_movie
GROUP BY m.title
HAVING COUNT(r.id_review) > 1;

3-Enunciado: Encuentra el nombre de los críticos y la cantidad de críticas que han realizado.
SELECT r.reviewer_name, COUNT(r.id_review) AS num_reviews
FROM reviews r
GROUP BY r.reviewer_name;

4. Encuentra las películas junto con sus géneros:
SELECT m.title, GROUP_CONCAT(g.name SEPARATOR ', ') AS genres
FROM movies m
INNER JOIN movies_genres mg ON m.id_movie = mg.id_movie
INNER JOIN genres g ON mg.id_genre = g.id_genre
GROUP BY m.title;

5.buscar el nombre de la pelicula y el rating maximo y minimo recibido
SELECT 
    m.title,
    MAX(r.rating) AS max_rating,
    MIN(r.rating) AS min_rating
FROM 
    movies m
LEFT JOIN 
    reviews r ON m.id_movie = r.id_movie
GROUP BY 
    m.title;
