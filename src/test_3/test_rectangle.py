from src.test_3.rectangle import Rectangle


def test_rectangle_area():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

def test_rectangle_perimeter():
    rect = Rectangle(4, 5)
    assert rect.perimeter() == 18