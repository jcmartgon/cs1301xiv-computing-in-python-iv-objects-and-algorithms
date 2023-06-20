# Jesus Carlos Martinez Gonzalez
# 19/06/23
# Capital Consonants

# Write a function called count_capital_consonants. This
# function should take as input a string, and return as output
# a single integer. The number the function returns should be
# the count of characters from the string that were capital
# consonants. For this problem, consider Y a consonant.
#
# For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def count_capital_consonants(s):
    count = 0
    for letter in s:
        if letter not in vowels and letter.isupper():
            count += 1
    return count


# The lines below will test your code. Feel free to modify
# them. If your code is working properly, these will print
# the same output as shown above in the examples.
print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))
