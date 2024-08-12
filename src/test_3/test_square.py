from src.test_3.square import Square


def test_square():
    square = Square(4)
    assert square.width == 4
    assert square.height == 4
    assert square.area() == 16
    assert square.perimeter() == 16