import pytest



def test_not_skip():
    assert 3 == 3, 'Not equal!'

@pytest.mark.skip('Заблокирован багом AXTM=1690')
def test_skip():
    assert 1 == 1, 'Not equal!'