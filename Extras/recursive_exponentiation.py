# Jesus Carlos Martinez Gonzalez
# 20/06/23
# Recursive Exponentiation

# Exponentiation (that is, raising a number to an exponent)
# can be thought of as a recursive process. 2 to the 3rd
# power, for instance, is the same as 2 times 2 to the 2nd
# power. 2 to the 2nd is the same as 2 times 2 to the 1st
# power. 2 to the 1st is the same as 2 times 2 to the 0th
# power. Anything to the 0th power is 1.
#
# Write a function called rec_exp. rec_exp should have two
# parameters: the first is the base, and the second is the
# power. For example, rec_exp(2, 3) would raise 2 to the 3rd
# power. rec_exp should return the result of the expression.
# For example:
#
# rec_exp(2, 3) -> 8 (2 to the 3rd)
# rec_exp(3, 4) -> 81 (3 to the 4th)
# rec_exp(8, 2) -> 64 (8 to the 2nd)
#
# You must implement rec_exp with recursion. You may not use
# any of the other mechanisms for raising a base to an exponent
# (e.g. pow, **).
#
# HINT: A RecursionError arises if your recursive calls never
# end. If you encounter a RecursionError, check your base case!


def rec_exp(base, power):
    if power == 0:
        return 1
    return base * rec_exp(base, power - 1)


# The lines below will test your code. If your function is
# correct, they will print 8, 81, 64.
print(rec_exp(2, 3))
print(rec_exp(3, 4))
print(rec_exp(8, 2))
