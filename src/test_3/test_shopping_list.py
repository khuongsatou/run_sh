from src.test_3.shopping_list import ShoppingList


def test_add_item():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.add_item("Bread")
    assert shopping_list.items == ["Milk", "Bread"]

def test_remove_item():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.add_item("Bread")
    shopping_list.remove_item("Milk")
    assert shopping_list.items == ["Bread"]

def test_total_items():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.add_item("Bread")
    assert shopping_list.total_items() == 2
    shopping_list.remove_item("Milk")
    assert shopping_list.total_items() == 1