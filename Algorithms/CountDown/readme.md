# Exercise Tracker

## Problem Description

We've written a function below called count_down(). This function takes an int parameter, start, and prints every number from that start to 0. The way we've written it uses recursion. Below that funtion, write a function that does the exact same thing, but do not use recursion.

The purpose of this exercise is for you to recognize some example instances in which you can use recursion, and what differences can be seen in the actual code.

Make sure to actually print 0 as the last number!

## My solution

#### count_down.py

```python
def count_down2(start):
    for i in range(start, -1, -1):
        print(i)
```

#### test_count_down.py

```python
import pytest
from count_down import count_down2


def test_count_down(capfd):
    count_down2(5)
    captured = capfd.readouterr()
    assert captured.out == "5\n4\n3\n2\n1\n0\n"

```

## Tests

![All passed](./resources/tests.png)

## Score

![All good](./resources/score.png)

## Usage

1. Run 'python count_down.py'.
2. Input a value.