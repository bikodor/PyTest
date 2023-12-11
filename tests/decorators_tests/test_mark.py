import pytest
# Запускать маркеры через консоль добавить ' -k development' без кавычек если надо запустить метку для дева
# Запустить марки не дева ' -k "not development"'
# Запустить марки и дев и тест (не одновременно имеющие оба значения) ' -k "development or testing" '
# Запустить марки и дев и тест (имеющие одновременно оба значения) ' -k "development and testing" '
# Записывать новые марки (как сейчас development) в корневой папке в файле pytest.ini
@pytest.mark.development
def test_dev():
    assert 1 == 1, 'Not equal'

# Записывать новые марки (как сейчас testing) в корневой папке в файле pytest.ini
@pytest.mark.testing
def test_test():
    assert 2 == 2, "Not equal"

# Записывать новые марки (как сейчас production) в корневой папке в файле pytest.ini
@pytest.mark.production
def test_prod():
    assert 3 == 3, "Not equal"

# Запустится если указать марку отдельно и дева, и теста
@pytest.mark.development
@pytest.mark.testing
def test_for_dev_and_test():
    assert 4 == 4, "Not equal"