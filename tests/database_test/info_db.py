from db import session
from sqlalchemy.sql.expression import desc
import tables

result_1 = session.query(tables.Films.film_id, tables.Films.title).first()
#даёт первый найденный результат
result_2 = session.query(tables.Films.film_id, tables.Films.title).all()
#выводит все результаты выборки
result_3 = session.query(tables.Films.film_id, tables.Films.title).one_or_none()
#должен соответствовать конкретному условию, ищем конкретное что-то, возвращает либо его либо ничего (что-то одно)
#возвращает не массивом
result_4 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id == 180).one_or_none()
#возвращает по фильтру фильм с 180 id
result_5 = session.query(tables.Films.film_id, tables.Films.title).filter(
    tables.Films.film_id < 150,
    tables.Films.film_id > 100
).all()
#можно юзать несколько фильтров, вернёт фильмы с id больше 100 но меньше 150
films_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 180).subquery()
#subquery показывает какой запрос на языке SQL отправляется в БД
result_6 = session.query(tables.Films.title).filter(tables.Films.film_id.in_(films_ids)).all()
#фильтруем по уже созданному запросу в films_id (создали в одной переменной запрос, заселектили его а потом использовали в другом благодаря in_
films_order_1 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).all()
#сортирует по id(как в SQL order by)
films_order_2 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(desc(tables.Films.film_id)).all()
#сортирует в обратном порядке (как в SQL desc)
result_7 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).limit(1).all()
#делает лимит вывода (limit(1) выводит только одну первую строку)
result_7 = session.query(tables.Films.film_id, tables.Films.title).filter(tables.Films.film_id > 180).order_by(tables.Films.film_id).limit(1).offset(1).all()
#offset(n) пропускает n количество строк (должен вывести фильмы с 4, 5 и 6 id, offset(1), значит выведет 5 и 6


print(result_1)