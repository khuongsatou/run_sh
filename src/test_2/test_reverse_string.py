from src.test_2.reverse_string import reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""