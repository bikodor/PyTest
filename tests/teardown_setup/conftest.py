# Этот файлик conftest все фикстуры которые в нем
# Будут доступны только папке user

import pytest

from random import randrange


@pytest.fixture
def make_number():
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number  # До yield фикстура выполняется до теста
    # После yield выполняется после теста, можно передавать атрибуты можно нет
    print(f"Number at home {number}")