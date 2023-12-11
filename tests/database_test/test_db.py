import tables


def test_get_data_films(get_db_session):
    data = get_db_session.query(tables.Films).first()
    # print(data.title) запринтит title

def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.Films, (tables.Films.film_id == 3))

def test_try_to_add_testdata(get_db_session, get_add_method):
    new_film = {"title": "Зелёный Слоник"}
    film = tables.Films(**new_film)
    get_add_method(get_db_session, film)
