import pytest
from src.test_6.bank_account import BankAccountBook, Bank  # Giả sử lớp BankAccount và Bank được lưu trong tệp bank_module.py

def test_bank_initialization():
    bank = Bank()
    assert bank.accounts == []

def test_add_account():
    bank = Bank()
    account = BankAccountBook("Alice", 100)
    bank.add_account(account)
    assert bank.accounts == [account]

def test_remove_account():
    bank = Bank()
    account1 = BankAccountBook("Alice", 100)
    account2 = BankAccountBook("Bob", 200)
    bank.add_account(account1)
    bank.add_account(account2)
    bank.remove_account(account1)
    assert bank.accounts == [account2]

def test_get_total_balance():
    bank = Bank()
    account1 = BankAccountBook("Alice", 100)
    account2 = BankAccountBook("Bob", 200)
    bank.add_account(account1)
    bank.add_account(account2)
    assert bank.get_total_balance() == 300

def test_find_account_by_owner():
    bank = Bank()
    account1 = BankAccountBook("Alice", 100)
    account2 = BankAccountBook("Bob", 200)
    bank.add_account(account1)
    bank.add_account(account2)
    found_account = bank.find_account_by_owner("Alice")
    assert found_account == account1
    not_found_account = bank.find_account_by_owner("Charlie")
    assert not_found_account == None
