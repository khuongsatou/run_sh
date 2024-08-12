from src.test_2.count_words import count_words


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("a b c") == 3
    assert count_words("") == 0
    assert count_words("one") == 1