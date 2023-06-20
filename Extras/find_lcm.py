# Jesus Carlos Martinez Gonzalez
# 20/06/23
# Find LCM

# The Least Common Multiple (LCM) of two numbers is the
# smallest number that divides by both those two numbers
# evenly. For example, the Least Common Multiple of 4 and
# 6 is 12: 12 divides evenly by both 4 and 6, and no
# smaller number does.
#
# The smallest possible LCM for two numbers is the
# larger of the two numbers; for example, the LCM for
# 2 and 10 is 10, because 10 divides evenly by 2.
#
# The largest possible LCM for two numbers is the product
# of the two numbers; for example, the LCM for 2 and 7
# is 14. By definition, the product of the two numbers
# will always be divisible by both.
#
# Write a function called find_lcm. find_lcm should have
# two parameters, both integers. find_lcm should return
# the Least Common Multiple of those two numbers.
#
# For example:
#
# find_lcm(2, 10) -> 10
# find_lcm(2, 7) -> 14
# find_lcm(4, 6) -> 12
# find_lcm(5, 5) -> 5
#
# You may assume the second number is at least as big as
# the first number (i.e. if the numbers are not equal, the
# second number is the larger one).


def find_gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n


def find_lcm(n, m):
    return (n * m) // find_gcd(n, m)


# The lines below will test your code. Feel free to modify
# them. If your code is working properly, these will print
# the same output as shown above in the examples.
print(find_lcm(2, 10))
print(find_lcm(2, 7))
print(find_lcm(4, 6))
print(find_lcm(5, 5))
