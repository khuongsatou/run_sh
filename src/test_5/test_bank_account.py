import pytest
from src.test_5.bank_account import BankAccount  # Giả sử lớp BankAccount được lưu trong tệp bank_account.py

def test_initialization():
    account = BankAccount("Alice", 100)
    assert account.owner == "Alice"
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount("Alice", 100)
    assert account.deposit(50) == True
    assert account.get_balance() == 150
    assert account.deposit(-10) == False
    assert account.get_balance() == 150

def test_withdraw():
    account = BankAccount("Alice", 100)
    assert account.withdraw(50) == True
    assert account.get_balance() == 50
    assert account.withdraw(100) == False
    assert account.get_balance() == 50

def test_transfer():
    account1 = BankAccount("Alice", 100)
    account2 = BankAccount("Bob", 50)
    assert account1.transfer(50, account2) == True
    assert account1.get_balance() == 50
    assert account2.get_balance() == 100
    assert account1.transfer(100, account2) == False
    assert account1.get_balance() == 50
    assert account2.get_balance() == 100

def test_invalid_operations():
    account = BankAccount("Alice", 100)
    assert account.deposit(0) == False
    assert account.withdraw(0) == False
    assert account.withdraw(-10) == False


