# # 1. Actores que tienen de primer nombre ‘Scarlett’.
#select * from actor
#where nombre = 'Scarlett';

## # 2. Actores que tienen de apellido ‘Johansson’.
select apellidos from actor
where apellidos = 'Johansson';

## # 3. Actores que contengan una ‘U’ en su nombre.
select nombre from actor
where nombre like '%u%';

## # 4. Actores que contengan una ‘U’ en su nombre y una ‘A’ en su apellido.
select nombre, apellidos from actor
where nombre like '%u%' and apellidos like '%a%';

## # 5. Actores que contengan dos ‘O’ en su nombre y una ‘A’ en su apellido.
select nombre, apellidos from actor
where nombre like '%o%o%' and apellidos like '%a%';

## # 6. Actores donde su tercera letra sea ‘B’.
select nombre from actor
where nombre like '__b%';

## # 7. Ciudades que empiezan por ‘a’.
select nombre from ciudad
where nombre like 'a%';

## # 8. Ciudades que acaban por ‘s’.
select nombre from ciudad
where nombre like '%s';

## # 9. Ciudades del país cuyo ID es 6.
select nombre, id_pais from ciudad
where id_pais = 6;

## # 10. Ciudades del pais ‘Spain’.
select ciudad.nombre, pais.nombre
from ciudad
join pais on ciudad.id_pais = pais.id_pais
where pais.nombre = "Spain"; 
#es más eficiente con muchos más datos

select ciudad.nombre, pais.nombre
from ciudad,pais
where ciudad.id_pais = pais.id_pais and pais.nombre = "Spain";

select ciudad.nombre as ciudad ;

## # 11. Ciudades con nombres compuestos.
select nombre from ciudad
where nombre like '% %';

## # 12. Películas con una duración entre 80 y 100.
select duracion, titulo from pelicula
where duracion between 80 and 100;

select titulo, duracion from pelicula
where duracion >= 80 and duracion <= 100;


## # 13. Películas con un rental_rate entre 1 y 3.
select titulo, rental_rate from pelicula
where rental_rate between 1 and 3;

## # 14. Películas con un título de más de 12 letras.
select titulo from pelicula
where length(titulo) > 12;

## # 15. Películas con una clasificación de PG o G.
select titulo, clasificacion from pelicula
where clasificacion = "PG" or clasificacion = "G";

## # 16. Películas que no tengan una clasificación de NC-17.
select titulo, clasificacion from pelicula
where clasificacion != "NC-17";

## # 17. Películas con una clasificación PG y duración de más de 120.
select titulo, clasificacion, duracion from pelicula
where clasificacion = "PG" and duracion > 120;

## # 18. ¿Cuántos actores hay?
select count(id_actor) as cantidad_actores
from actor;

## # 19. ¿Cuántas ciudades tiene el pais ‘Spain’?
select pais.nombre as pais, count(ciudad.id_pais)
from ciudad
join pais on ciudad.id_pais = pais.id_pais
group by 1;

#revisar para Spain

## # 20. ¿Cuántos países hay que empiezan por ‘a’?
select count(*) as cantidad from pais
where nombre like "A%";

## # 21. Promedio de duración de películas con PG.
select round(avg(duracion),2) as promedio from pelicula
where clasificacion = "PG";

## # 22. Suma de rental_rate de todas las películas.
select sum(rental_rate) as suma_rental_rate from pelicula;

## # 23. Duración de la película más larga.
select max(duracion) as duracion_mas_larga from pelicula;

## # 24. Duración de la película más corta.
select min(duracion) as duracion_mas_corta from pelicula;

## # 25. Mostrar las ciudades del pais Spain (multitabla).

## # 26. Mostrar el nombre de la película y el nombre de los actores. Debe devolver 5462 resultados.
select titulo, nombre, apellidos
from pelicula
join pelicula_actor on pelicula.id_pelicula = pelicula_actor.id_pelicula
join actor on actor.id_actor = pelicula_actor.id_actor
order by titulo,3,2;

## # 27. Mostrar el nombre de la película y el de sus categorías. Debe devolver 1000 resultados.


## # 28. Mostrar el pais, la ciudad y dirección de cada empleado. Debe devolver 5 resultados.
select apellidos, e.nombre, p.nombre as pais, c.nombre as ciudad
from empleado as e
join direccion as d on e.id_direccion = d.id_direccion
join ciudad as c on d.id_ciudad = c.id_ciudad
join pais as p on c.id_pais = p.id_pais;

## # 29. Mostrar el pais, la ciudad y dirección de cada cliente. Debe devolver 45 resultados.
select apellidos, clie.nombre, p.nombre as pais, c.nombre as ciudad
from cliente as clie
join direccion as d on clie.id_direccion = d.id_direccion
join ciudad as c on d.id_ciudad = c.id_ciudad
join pais as p on c.id_pais = p.id_pais;

## # 30. Cantidad de películas de cada clasificación. Debe devolver 5 resultados.
select clasificacion, count(*)
from pelicula
group by 1
order by 1;

## # 31. ¿Cuántas películas ha realizado el actor ED CHASE? Debe devolver 1 resultado.

## # 32. Media de duración de las películas de cada categoría. Debe devolver 16 resultados.
## # 33. Cantidad de películas de cada categoría. Debe devolver 16 resultados.
## # 34. Muestra el nombre y apellido de todos los actores. Debe devolver 200 resultados.
## # 35. Muestra el nombre y apellido de cada actor en una sola columna, en mayúscula. Nombra la columna "Nombre del actor". Debe devolver 200 resultados.
## # 36. Muestra el ID, nombre y apellido de un actor, de quien solo tienes el nombre "John". Debe devolver 1 resultado.
## # 37. Listar los actores cuyo apellido contenga "GE". Debe devolver 13 resultados.
## # 38. Listar los actores cuyo apellido contenga "RA". Ordena las filas por apellido y nombre (en ese orden). Debe devolver 8 resultados.
## # 39. Usando la función IN, muestra el nombre y apellido de todos los clientes llamados "Kelly", "Paula" o "Alice". Debe devolver 4 resultados.
## # 40. Muestra el apellido y la cantidad de actores que tienen ese apellido, ordenados de mayor a menor ocurrencia. Debe devolver 121 resultados.
## # 41. Muestra el apellido y la cantidad de actores que tienen ese apellido, pero solo los apellidos compartidos por dos o más actores. Debe devolver 55 resultados.
## # 42. Usando joins, muestra el nombre, apellido y dirección de cada miembro del staff. Debe devolver 5 resultados.
## # 43. Muestra el total de dinero recaudado por cada empleado durante agosto del 2005. Debe devolver 2 resultados.
## # 44. Mostrar la cantidad de actores por cada película. Debe devolver 1000 resultados.
## # 45. ¿Cuántas copias hay inventariadas en el sistema de la película "Hunchback Impossible"? Debe devolver 1 resultado con cantidad = 6.
## # 46. Mostrar el total de dinero pagado por cada cliente, solo si ha realizado compras. Ordena los clientes por apellido de forma ascendente. Debe devolver 599 resultados.
## # 47. Se debe realizar una campaña de marketing en Japón ("Japan"). Para esto necesitas el nombre y correo electrónico de todos los clientes japoneses. Debe devolver 4 resultados.
## # 48. Identifica todas las películas categorizadas como familiares (categoría "familiar"). Debe devolver 69 resultados.
## # 49. Listar las películas más alquiladas en orden descendente. Debe devolver 1000 resultados.
## # 50. Mostrar el dinero recaudado por cada almacén. Debe devolver 121 resultados.