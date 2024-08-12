from src.test_3.person import Person


def test_person_initialization():
    person = Person("Alice", 30)
    assert person.name == "Alice"
    assert person.age == 30

def test_person_greet():
    person = Person("Alice", 30)
    assert person.greet() == "Hello, my name is Alice and I am 30 years old."

def test_person_update_attributes():
    person = Person("Alice", 30)
    person.name = "Bob"
    person.age = 25
    assert person.name == "Bob"
    assert person.age == 25