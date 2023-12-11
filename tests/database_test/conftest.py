from db import Session
import pytest

@pytest.fixture
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close() #чтобы не случилось дропаем сессию

def delete_test_data(session, table, filter_data):
    session.query(table).filter(filter_data).delete()
    session.commit()

def add_method(session, item):
    session.add(item)
    session.commit()

@pytest.fixture
def get_add_method():
    return add_method


@pytest.fixture
def get_delete_method():
    return delete_test_data
