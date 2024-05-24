select m.id_movie, title, release_date, director, coalesce(genre.name, m.title) as genero
from movie m
left join movie_genre mg on m.id_movie = mg.id_movie
left join genre on mg.id_genre = genre.id_genre 
where title like '%'
order by id_movie, release_date asc;

select m.title, count(mg.id_genre)
from movie m
left join movie_genre mg on m.id_movie = mg.id_movie
group by m.title;

select m.title, round(avg(r.rating), 2) rating_promedio
from movie m 
left join review r on m.id_movie = r.id_movie
where title like 'E%'
group by m.title
having avg(r.rating) > 4.8;

