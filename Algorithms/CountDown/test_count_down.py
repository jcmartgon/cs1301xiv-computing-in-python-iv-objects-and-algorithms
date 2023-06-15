# Jesus Carlos Martinez Gonzalez
# 14/06/2023
# Countdown

import pytest
from count_down import count_down2


def test_count_down(capfd):
    count_down2(5)
    captured = capfd.readouterr()
    assert captured.out == "5\n4\n3\n2\n1\n0\n"
