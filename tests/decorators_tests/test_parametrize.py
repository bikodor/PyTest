import pytest

@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (5, 2, 7),
    (-1, 6, 5),
    # (-3, -2, 5) выбьет ошибку, тк -5 отрицательное
])
def test_positive_number(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) >= 0, "This Number not positive"