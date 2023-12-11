import pytest


@pytest.fixture() #работает до теста самого
def say_hello():
    print("Hello, its me")
    return 14

# @pytest.fixture(scope='function')
# #scope='function' значит, что фикстура
# # будет работать каждый раз, а session только один раз
# # и результат сохраняется и всегда передаваться
# # будет только он, даже если поменяем значения
# # подробнее можно чекнуть перейдя в fixture
# def say_hello():
#     print("Hello, its me")
#     return 14

# @pytest.fixture(autouse=True)
# autouse=True значит, что фикстура будет
# выполняться автоматически, даже без ее вызова
# опасна, редко нужна, но хорошо работает с session
# но для того чтобы выводить параметр, нужно все равно
# вызывать его
# def say_hello():
#     print("Hello, its me")
#     return 14
