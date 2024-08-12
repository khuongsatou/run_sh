import pytest
from src.test_2.max import find_max


def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([-1, -2, -3]) == -1
    with pytest.raises(ValueError):
        find_max([])
        