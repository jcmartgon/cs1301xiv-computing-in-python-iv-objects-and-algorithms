# Jesus Carlos Martinez Gonzalez
# 22/05/2023
# Phone class

from phone import Phone


# Storage
def test_storage():
    phone = Phone()
    assert phone.storage == 128


# Color
def test_color():
    phone = Phone()
    assert phone.color == "red"
