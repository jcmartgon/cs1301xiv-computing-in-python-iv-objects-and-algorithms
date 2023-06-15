# Jesus Carlos Martinez Gonzalez
# 14/06/2023
# Exponent

from exponent import exponent_calc


def test_exponent():
    assert exponent_calc(5, 3) == 125
    assert exponent_calc(5, 0) == 1
    assert exponent_calc(0, 100) == 0
