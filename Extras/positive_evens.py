# Jesus Carlos Martinez Gonzalez
# 17/06/2023
# Positive Evens

# Write a function called count_positive_evens. This function
# should take as input a list of integers, and return as
# output a single integer. The number the function returns
# should be the count of numbers from the list that were both
# positive and even.
#
# For example:
#
# count_positive_evens([5, 7, 9, 8, -1, -2, -3]) -> 1
# count_positive_evens([2, 4, 6, 8, 10, 12, 15]) -> 6
# count_positive_evens([-2, -4, -6, -8, -10, 1]) -> 0
#
# 0 should be not counted as a positive even number.
#
# Hint: Remember, even numbers are numbers that have a
# remainder of 0 when divided by 2.


def count_positive_evens(lst):
    count = 0
    for i in range(len(lst)):
        elem = lst[i]
        if elem > 0 and elem % 2 == 0:
            count += 1
    return count


# The lines below will test your code. Feel free to modify
# them. If your code is working properly, these will print
# the same output as shown above in the examples.
print(count_positive_evens([5, 7, 9, 8, -1, -2, -3]))
print(count_positive_evens([2, 4, 6, 8, 10, 12, 15]))
print(count_positive_evens([-2, -4, -6, -8, -10, 1]))
