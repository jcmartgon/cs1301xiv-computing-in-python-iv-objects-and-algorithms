# Linear

## Problem Description

Write a function called linear() that takes two parameters - a list of strings and a string. Write this function so that it returns the first index at which the string is found within the list if the string is found, or False if it is not found. You do not need to worry about searching for the search string inside the individual strings within the list: for example, linear(["bobby", "fred"], "bob") should return False, but linear(["bob", "fred"], "bob") should return 0.

Use a linear search algorithm (not as scary as it sounds).
Do not use the list method index -- in this exercise, you're actually implementing the way the index method works!

## My solution

#### linear.py

```python
def linear(lst, string):
    for i in range(len(lst)):
        if lst[i] == string:
            return i
    return False
```

#### test_linear.py

```python
from linear import linear

ordered_list = [str(i) for i in range(100)]
reversed_list = [str(i) for i in range(99, -1, -1)]


def test_search_ordered_list():
    assert linear(ordered_list, "5") == 5
    assert linear(ordered_list, "99") == 99


def test_search_reversed_list():
    assert linear(reversed_list, "5") == 94
    assert linear(reversed_list, "99") == 0

```

## Tests

![All passed](./resources/tests.png)

## Score

![All good](./resources/score.png)

## Usage

1. Run 'python linear.py'.