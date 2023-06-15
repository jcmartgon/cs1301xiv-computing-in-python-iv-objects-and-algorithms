# Jesus Carlos Martinez Gonzalez
# 14/06/2023
# Linear

from linear import linear

ordered_list = [str(i) for i in range(100)]
reversed_list = [str(i) for i in range(99, -1, -1)]


def test_search_ordered_list():
    assert linear(ordered_list, "5") == 5
    assert linear(ordered_list, "99") == 99


def test_search_reversed_list():
    assert linear(reversed_list, "5") == 94
    assert linear(reversed_list, "99") == 0
