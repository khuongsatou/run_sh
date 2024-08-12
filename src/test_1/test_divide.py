import pytest
from src.test_1.divide import divide


def test_divide():
    assert divide(4, 2) == 2
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(1, 0)