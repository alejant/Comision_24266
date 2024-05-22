-- Crear la base de datos
CREATE database cac_movies_bd;

-- Correr todo lo siguiente en un query que esté conectado en la base de datos anterior.
-- Crear la tabla genre
CREATE TABLE genre (
  id_genre SERIAL PRIMARY KEY,
  name VARCHAR(20) NOT NULL
);

-- Crear la tabla movie
CREATE TABLE movie (
  id_movie SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  release_date DATE,
  director VARCHAR(50)
);

-- Crear la tabla review
CREATE TABLE review (
  id_review SERIAL PRIMARY KEY,
  id_movie INT REFERENCES movie(id_movie) ON DELETE CASCADE ON UPDATE CASCADE,
  reviewer_name VARCHAR(100),
  comment TEXT,
  rating DECIMAL(4, 2)
);

-- Crear índices para la tabla review
CREATE INDEX fk_movie_idx ON review(id_movie);

-- Crear la tabla movie_genre
CREATE TABLE movie_genre (
  id_movie_genre SERIAL PRIMARY KEY,
  id_movie INT NOT NULL REFERENCES movie(id_movie) ON DELETE CASCADE ON UPDATE CASCADE,
  id_genre INT NOT NULL REFERENCES genre(id_genre) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Crear índices para la tabla movie_genre
CREATE INDEX fk_movie_genre_movie_idx ON movie_genre(id_movie);
CREATE INDEX fk_movie_genre_genre_idx ON movie_genre(id_genre);

-- Inserciones en la tabla genre
INSERT INTO genre (name) VALUES 
('Acción'),
('Comedia'),
('Drama'),
('Ciencia Ficción'),
('Romance'),
('Terror'),
('Aventura'),
('Animación'),
('Fantasía'),
('Documental');

-- Inserciones en la tabla movie
INSERT INTO movie (title, release_date, director) VALUES 
('El Señor de los Anillos: La Comunidad del Anillo', '2001-12-19', 'Peter Jackson'),
('Pulp Fiction', '1994-10-14', 'Quentin Tarantino'),
('Titanic', '1997-12-19', 'James Cameron'),
('Forrest Gump', '1994-07-06', 'Robert Zemeckis'),
('El Rey León', '1994-06-24', 'Roger Allers, Rob Minkoff'),
('El Padrino', '1972-03-24', 'Francis Ford Coppola'),
('Interestelar', '2014-11-07', 'Christopher Nolan'),
('Harry Potter y la piedra filosofal', '2001-11-30', 'Chris Columbus'),
('La La Land', '2016-12-09', 'Damien Chazelle'),
('El club de la lucha', '1999-10-15', 'David Fincher');

-- Inserciones en la tabla movie_genre
INSERT INTO movie_genre (id_movie, id_genre) VALUES 
(1, 1), (1, 7),
(2, 3), (2, 8),
(3, 5), (3, 3),
(4, 3),
(5, 8), (5, 7),
(6, 3), (6, 8),
(7, 4),
(8, 9), (8, 7),
(9, 10), (9, 3),
(10, 3), (10, 8);

-- Inserciones en la tabla review
INSERT INTO review (id_movie, reviewer_name, comment, rating) VALUES 
(1, 'María', 'Una gran película de aventuras.', 4.5),
(1, 'Juan', 'El inicio de una gran saga.', 4.8),
(1, 'Luis', 'Impresionante, ¡quiero más elfos!', 4.7),
(3, 'Ana', 'Una historia de amor inolvidable.', 4.2),
(3, 'Carlos', 'Una experiencia cinematográfica épica.', 4.6),
(4, 'Pedro', 'Una película que te llega al corazón.', 4.6),
(4, 'Laura', 'Una película que te hace sentir muchas emociones.', 4.7),
(6, 'Martín', 'Un clásico indiscutible del cine.', 4.9),
(7, 'Elena', 'Una obra maestra del sci-fi.', 4.8),
(7, 'Luisa', 'Un viaje emocionante a través del espacio.', 4.9),
(8, 'Javier', 'El inicio de una gran saga.', 4.7),
(9, 'Lucía', 'Un musical moderno y encantador.', 4.4),
(10, 'Marta', 'Una película que te hace reflexionar.', 4.3);
