# Jesus Carlos Martinez Gonzalez
# 18/06/23
# Pig Latin

# Pig Latin is a fictitious language. To translate a word into
# Pig Latin, you would take the consonants up until the first
# vowel, move them to the end, and add "ay" to the end.
#
# For example:
#
# pig -> igpay
# david -> avidday
# trash -> ashtray
# scram -> amscray
# translate -> anslatetray
#
# Write a function called to_pig_latin. to_pig_latin will take
# as input a single word, and return the Pig Latin version of
# the word.
#
# For the purposes of this problem, only a, e, i, o, and u are
# vowels: y is a consonant. You may assume that the word will
# start with at least one consonant, that the letters to move to
# the end will always be the consonants until the first vowel,
# and that the string will be all lower-case.

vowels = ["a", "e", "i", "o", "u"]


def to_pig_latin(word):
    new = ""
    for i, char in enumerate(word):
        if char not in vowels:
            new += char
        else:
            new = word[i:] + new + "ay"
            break
    return new


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print the same results as in the examples above.
print(to_pig_latin("pig"))
print(to_pig_latin("david"))
print(to_pig_latin("trash"))
print(to_pig_latin("scram"))
print(to_pig_latin("translate"))
