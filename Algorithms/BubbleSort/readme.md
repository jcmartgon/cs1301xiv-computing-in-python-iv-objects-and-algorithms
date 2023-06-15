# Bubble Sort

## Problem Description

We've written the function, sort_with_bubbles, below. It takes in one list parameter, lst. However, there are two problems in our current code:
- There's a missing line
- There's a semantic error (the code does not raise an error message, but it does not perform correctly)

Find and fix these problems! Note that you should only need to change or add code where explicitly indicated.

## My solution

#### sort_with_bubble.py

```python
def sort_with_bubbles(lst):
    # Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True

    # Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        # Start off assuming a swap did not occur
        swap_occurred = False

        # For every item in the list except the last one...
        for i in range(len(lst) - 1):
            # If the item should swap with the next item...
            if lst[i] > lst[i + 1]:
                # Then, swap them! But these lines aren't
                # quite right: fix this code!
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap_occurred = True

                # One more line is needed here; add it!

    return lst
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

1. Run 'python bubble_sort.py'.