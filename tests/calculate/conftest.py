# Этот файлик conftest все фикстуры которые в нем
# Будут доступны только папке calculate

import pytest

def _calculate(a, b):
    return a + b



@pytest.fixture
def calculate():
    return _calculate # ВАЖНО! БЕЗ ()

