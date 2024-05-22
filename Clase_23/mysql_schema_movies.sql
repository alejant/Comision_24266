CREATE SCHEMA `cac_movies_bd` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE `cac_movies_bd`.`genre` (
  `id_genre` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NULL,
  PRIMARY KEY (`id_genre`));

ALTER TABLE `cac_movies_bd`.`genre` 
CHANGE COLUMN `name` `name` VARCHAR(20) NOT NULL ;


CREATE TABLE `cac_movies_bd`.`movie` (
  `id_movie` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `release_date` DATE NULL,
  `director` VARCHAR(50) NULL,
  PRIMARY KEY (`id_movie`));

Tengo la siguiente estructura de una tabla, necesito que me facilites 20 sentencias INSERT de acuerdo a los registros de movie que me diste, puedes hacer que una movie tenga hasta 3 review y otras ninguna. Tienen que estar en español
CREATE TABLE `cac_movies_bd`.`review` (
  `id_review` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NULL,
  `reviewer_name` VARCHAR(100) NULL,
  `comment` TEXT NULL,
  `rating` DECIMAL(4,2) NULL,
  PRIMARY KEY (`id_review`));

ALTER TABLE `cac_movies_bd`.`review` 
ADD INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE;
;
ALTER TABLE `cac_movies_bd`.`review` 
ADD CONSTRAINT `fk_movie`
  FOREIGN KEY (`id_movie`)
  REFERENCES `cac_movies_bd`.`movie` (`id_movie`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;


CREATE TABLE `cac_movies_bd`.`movie_genre` (
  `id_movie_genre` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NOT NULL,
  `id_genre` INT NOT NULL,
  PRIMARY KEY (`id_movie_genre`),
  INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE,
  INDEX `fk_genre_idx` (`id_genre` ASC) VISIBLE,
  CONSTRAINT `fk_mg_movie`
    FOREIGN KEY (`id_movie`)
    REFERENCES `cac_movies_bd`.`movie` (`id_movie`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_mg_genre`
    FOREIGN KEY (`id_genre`)
    REFERENCES `cac_movies_bd`.`genre` (`id_genre`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

/* INSERTS */
INSERT INTO genre (name) VALUES ('Acción');
INSERT INTO genre (name) VALUES ('Comedia');
INSERT INTO genre (name) VALUES ('Drama');
INSERT INTO genre (name) VALUES ('Ciencia Ficción');
INSERT INTO genre (name) VALUES ('Romance');
INSERT INTO genre (name) VALUES ('Terror');
INSERT INTO genre (name) VALUES ('Aventura');
INSERT INTO genre (name) VALUES ('Animación');
INSERT INTO genre (name) VALUES ('Fantasía');
INSERT INTO genre (name) VALUES ('Documental');

INSERT INTO movie (title, release_date, director) VALUES ('El Señor de los Anillos: La Comunidad del Anillo', '2001-12-19', 'Peter Jackson');
INSERT INTO movie (title, release_date, director) VALUES ('Pulp Fiction', '1994-10-14', 'Quentin Tarantino');
INSERT INTO movie (title, release_date, director) VALUES ('Titanic', '1997-12-19', 'James Cameron');
INSERT INTO movie (title, release_date, director) VALUES ('Forrest Gump', '1994-07-06', 'Robert Zemeckis');
INSERT INTO movie (title, release_date, director) VALUES ('El Rey León', '1994-06-24', 'Roger Allers, Rob Minkoff');
INSERT INTO movie (title, release_date, director) VALUES ('El Padrino', '1972-03-24', 'Francis Ford Coppola');
INSERT INTO movie (title, release_date, director) VALUES ('Interestelar', '2014-11-07', 'Christopher Nolan');
INSERT INTO movie (title, release_date, director) VALUES ('Harry Potter y la piedra filosofal', '2001-11-30', 'Chris Columbus');
INSERT INTO movie (title, release_date, director) VALUES ('La La Land', '2016-12-09', 'Damien Chazelle');
INSERT INTO movie (title, release_date, director) VALUES ('El club de la lucha', '1999-10-15', 'David Fincher');


-- Asociación de "El Señor de los Anillos: La Comunidad del Anillo" con los géneros "Acción" y "Aventura"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (1, 1), (1, 7);

-- Asociación de "Pulp Fiction" con los géneros "Drama" y "Crimen"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (2, 3), (2, 8);

-- Asociación de "Titanic" con los géneros "Romance" y "Drama"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (3, 5), (3, 3);

-- Asociación de "Forrest Gump" con el género "Drama"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (4, 3);

-- Asociación de "El Rey León" con los géneros "Animación" y "Aventura"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (5, 8), (5, 7);

-- Asociación de "El Padrino" con los géneros "Drama" y "Crimen"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (6, 3), (6, 8);

-- Asociación de "Interestelar" con el género "Ciencia Ficción"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (7, 4);

-- Asociación de "Harry Potter y la piedra filosofal" con los géneros "Fantasía" y "Aventura"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (8, 9), (8, 7);

-- Asociación de "La La Land" con los géneros "Musical" y "Drama"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (9, 10), (9, 3);

-- Asociación de "El club de la lucha" con los géneros "Drama" y "Crimen"
INSERT INTO movie_genre (id_movie, id_genre) VALUES (10, 3), (10, 8);

-- Críticas para "El Señor de los Anillos: La Comunidad del Anillo"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (1, 'María', 'Una gran película de aventuras.', 4.5);
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (1, 'Juan', 'El inicio de una gran saga.', 4.8);
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (1, 'Luis', 'Impresionante, ¡quiero más elfos!', 4.7);

-- Crítica para "Titanic"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (3, 'Ana', 'Una historia de amor inolvidable.', 4.2);
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (3, 'Carlos', 'Una experiencia cinematográfica épica.', 4.6);

-- Crítica para "Forrest Gump"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (4, 'Pedro', 'Una película que te llega al corazón.', 4.6);
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (4, 'Laura', 'Una película que te hace sentir muchas emociones.', 4.7);

-- Crítica para "El Padrino"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (6, 'Martín', 'Un clásico indiscutible del cine.', 4.9);

-- Crítica para "Interestelar"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (7, 'Elena', 'Una obra maestra del sci-fi.', 4.8);
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (7, 'Luisa', 'Un viaje emocionante a través del espacio.', 4.9);
-- Crítica para "Harry Potter y la piedra filosofal"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (8, 'Javier', 'El inicio de una gran saga.', 4.7);

-- Crítica para "La La Land"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (9, 'Lucía', 'Un musical moderno y encantador.', 4.4);

-- Crítica para "El club de la lucha"
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES (10, 'Marta', 'Una película que te hace reflexionar.', 4.3);