# Exponent

## Problem Description

We've started a recursive function below called exponent_calc(). It takes in two integer parameters, base and expo. It should return the mathematical answer to base^expo. For example, exponent_calc(5, 3) should return 125: 5^3 = 125.

The code is almost done - we have our base case written. We know to stop recursing when we've reached the simplest form. When the exponent is 0, we return 1, because anything to the 0 power is 1. But we are missing our recursive call!

Fill in the marked line with the recursive call necessary to complete the function. Do not use the double-asterisk operator for exponentiation. Do not use any loops.

## My solution

#### exponent.py

```python
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base, expo - 1)
```

#### test_exponent.py

```python
from exponent import exponent_calc


def test_exponent():
    assert exponent_calc(5, 3) == 125
    assert exponent_calc(5, 0) == 1
    assert exponent_calc(0, 100) == 0
```

## Tests

![All passed](./resources/tests.png)

## Score

![All good](./resources/score.png)

## Usage

1. Run 'python exponent.py'.