from src.test_2.is_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("racecar") == True
    assert is_palindrome("") == True