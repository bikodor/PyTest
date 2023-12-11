import pytest

def _calculate(a, b):
    return a + b

@pytest.fixture
def calculate():
    return _calculate

