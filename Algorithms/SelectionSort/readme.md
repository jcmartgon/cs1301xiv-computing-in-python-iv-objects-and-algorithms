# Selection Sort

## Problem Description

We've written the function, sort_with_select, below. It takes in one list parameter, a_list. Our version of selection sort involves finding the minimum value and moving it to an earlier spot in the list.

However, some lines of code are blank. Complete these lines to complete the selection_sort function. You should only need to modify the section marked 'Write your code here!'

## My solution

#### selection_sort.py

```python
def sort_with_select(a_list):
    # For each index in the list...
    for i in range(len(a_list)):
        # Assume first that current item is already correct...
        minIndex = i

        # For each index from i to the end...
        for j in range(i + 1, len(a_list)):
            # Complete the reasoning of this conditional to
            # complete the algorithm! Remember, the goal is
            # to find the lowest item in the list between
            # index i and the end of the list, and store its
            # index in the variable minIndex.
            #
            if a_list[j] < a_list[minIndex]:
                minIndex = j

        # Save the current minimum value since we're about
        # to delete it
        minValue = a_list[minIndex]

        # Delete the minimum value from its current index
        del a_list[minIndex]

        # Insert the minimum value at its new index
        a_list.insert(i, minValue)

    # Return the resultant list
    return a_list
```

#### test_selection_sort.py

```python
from selection_sort import sort_with_select

sorted_list = [i for i in range(10000)]
reversed_list = [i for i in range(9999, -1, -1)]


def test_ordered_list():
    assert sort_with_select(sorted_list) == sorted_list


def test_revered_list():
    assert sort_with_select(reversed_list) == sorted_list

```

## Tests

![All passed](./resources/tests.png)

## Score

![All good](./resources/score.png)

## Usage

1. Run 'python selection_sort.py'.