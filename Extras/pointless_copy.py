# Jesus Carlos Martinez Gonzalez
# 18/06/023
# Pointless Copy

# Write a function called copy_pointlessly. This function should
# take two parameters, both strings. The first string is the
# filename of a file to which to write (output_file), and the
# second string is the filename of a file from which to read
# (input_file).
#
# copy_pointlessly should copy the contents of input_file into
# output_file, but make the following changes:
#
# - Replace all instances of the letter A (either capital or
#   lower case) with the at sign, @
# - Replace all instances of the letter M (either capital or
#   lower case) with the character sequence |\/|
# - Replace all instances of the letter W with the character
#   sequence \/\/
# - Replace all instances of the letter O (either capital
#   or lower case) with the numeral 0
# - Alternate the case for every remaining letter in the
#   string (hint: the_string.swapcase() returns the string
#   with the case of all letters swapped)
#
# For example, if these were the contents of input_file (the
# second parameter):
#
# This is some text. Woo text yay!
#
# Then to_upper_copy would write this text to output_file (the
# first parameter):
#
# tHIS IS S0|\/|E TEXT. \/\/00 TEXT Y@Y!
#
# No other characters should be changed. Note that the file
# to be copied will have multiple lines of text.
#
# We've included two files for you to test on: anInputFile.txt
# and anOutputFile.txt. The test code below will copy the text
# from the first file to the second. Feel free to modify the
# first to test different setups.

import string


def copy_pointlessly(output_file, input_file):
    infile = open(input_file, "r")

    content = infile.read()
    infile.close()

    outfile = open(output_file, "w")

    for char in content:
        if char in ["a", "A"]:
            outfile.write("@")
        elif char in ["m", "M"]:
            outfile.write("|\/|")
        elif char in ["w", "W"]:
            outfile.write("\/\/")
        elif char in ["o", "O"]:
            outfile.write("0")
        else:
            outfile.write(char.swapcase())

    outfile.close()


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, anOutputFile.txt should have the text:
# TEST @N @, TEST @N @
# TEST @N 0, TEST @N 0
# TEST @N |\/|, TEST @N |\/|
# TEST @ \/\/, TEST @ \/\/
copy_pointlessly("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")
