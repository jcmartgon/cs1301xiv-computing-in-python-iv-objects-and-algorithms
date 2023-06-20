# Jesus Carlos Martinez Gonzalez
# 20/06/23
# Obfuscatinator

# Write a function called deobfuscate. This function should
# take two parameters, both strings. The first string is the
# filename of a file to which to write (output_file), and the
# second string is the filename of a file from which to read
# (input_file).
#
# deobfuscate should copy the contents of input_file into
# output_file, with one twist: every pair of characters should
# be swapped. So, if the original file contained the text:
#
# BADCFEG
#
# Then the output file would contain the text ABCDEFG: the
# B and A swap; the D and C swap; and the F and E swap. The
# G is left alone; if there are an odd number of characters,
# leave the final character alone.
#
# This change should be applied to every character in the
# file: punctuation, spaces, and even line breaks. So, if the
# original file was:
#
# abc def
# ghi jkl
#
# Then the output file would contain:
#
# ba ced
# fhg ikjl
#
# Note that the c and space switch places, and that the f
# switches places with the line break immediately after it,
# which bumps the f down to the next line.
#
# We've included two files for you to test on: anInputFile.txt
# and anOutputFile.txt. The test code below will copy the text
# from the first file to the second. Feel free to modify the
# first to test different setups.


def deobfuscate(output_file, input_file):
    with open(input_file, "r") as file:
        input_text = file.read()

    output_text = ""
    for i in range(0, len(input_text), 2):
        if i + 1 < len(input_text):
            output_text += input_text[i + 1] + input_text[i]
        else:
            output_text += input_text[i]

    with open(output_file, "w") as file:
        file.write(output_text)


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, anOutputFile.txt should have the text:
# I'm a Ramblin' Wreck
# from Georgia Tech
deobfuscate("anOutputFile.txt", "anInputFile.txt")
print("Done running! Check anOutputFile.txt for the result.")


# If you accidentally erase anInputFile.txt, here's its original
# text to copy back in:
#'I m aaRbmil'nW erkcf
# or meGroig aeThc
