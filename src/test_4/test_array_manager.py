

from src.test_4.array_manager import ArrayManager


def test_array_manager_initialization():
    manager = ArrayManager([1, 2, 3])
    assert manager.array == [1, 2, 3]


def test_remove_element():
    manager = ArrayManager([1, 2, 3, 4])
    manager.remove_element(3)
    assert manager.array == [1, 2, 4]


def test_find_element():
    manager = ArrayManager([1, 2, 3, 4])
    assert manager.find_element(3) == True
    assert manager.find_element(5) == False


def test_sum_elements():
    manager = ArrayManager([1, 2, 3, 4])
    assert manager.sum_elements() == 10

def test_max_element():
    manager = ArrayManager([1, 2, 3, 4])
    assert manager.max_element() == 4

def test_min_element():
    manager = ArrayManager([1, 2, 3, 4])
    assert manager.min_element() == 1

def test_sort_ascending():
    manager = ArrayManager([4, 3, 2, 1])
    manager.sort_ascending()
    assert manager.array == [1, 2, 3, 4]

def test_sort_descending():
    manager = ArrayManager([1, 2, 3, 4])
    manager.sort_descending()
    assert manager.array == [4, 3, 2, 1]

def test_clear():
    manager = ArrayManager([1, 2, 3, 4])
    manager.clear()
    assert manager.array == []