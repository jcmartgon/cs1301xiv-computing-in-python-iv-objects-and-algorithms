# Jesus Carlos Martinez Gonzalez
# 23/05/2023
# CPerson

from person import Person


def test_no_parents():
    person = Person("Greg", 25)
    assert person.name == "Greg"
    assert person.age == 25
    assert person.father == None
    assert person.mother == None


def test_father():
    person = Person("Greg", 25, "Papa Greg")
    assert person.father == "Papa Greg"


def test_mother():
    person = Person("Greg", 25, mother="Moma Greg")
    assert person.mother == "Moma Greg"
