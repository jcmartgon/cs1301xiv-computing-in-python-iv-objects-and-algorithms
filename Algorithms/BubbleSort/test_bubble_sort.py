# Jesus Carlos Martinez Gonzalez
# 14/06/2023
# Bubble Sort

from bubble_sort import sort_with_bubbles

sorted_list = [i for i in range(10000)]
reversed_list = [i for i in range(9999, -1, -1)]


def test_ordered_list():
    assert sort_with_bubbles(sorted_list) == sorted_list


def test_revered_list():
    assert sort_with_bubbles(reversed_list) == sorted_list
