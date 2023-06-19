# Jesus Carlos Martinez Gonzalez
# 18/06/023
# Object Search

# Imagine you're writing a program to check attendance on a
# classroom roster. The list of students in attendance comes
# in the form of a list of instances of the Student class.
#
# You don't have access to the code for the Student class.
# However, you know that it has at least two attributes:
# first_name and last_name.
#
# Write a function called check_attendance. check_attendance
# should take three parameters: a list of instances of
# Student representing the students in attendance, a first
# name as a string, and a last name as a string (in that
# order).
#
# The function should return True if any instance in the
# list has the same first and last name as the two
# arguments. It should return False otherwise.
#
# You may assume that the list of students is sorted
# alphabetically, by last name and then by first name. This
# allows you to solve this with a binary search. However,
# you may also solve this problem with a linear search if
# you would prefer.


# The next comment block representing binary search should work but some of the test cases don't follow the assumptions mentioned above so it fails; linear search works regardless.
"""
def check_attendance(students, first_name, last_name):
    left = 0
    right = len(students) - 1
    
    while left <= right:
        mid = (left + right) // 2
        curr = students[mid]
        
        if curr.first_name == first_name and curr.last_name == last_name:
            return True
        if curr.last_name < last_name or (curr.last_name == last_name and curr.first_name < first_name):
            left = mid + 1
        else:
            right = mid - 1
    return False
"""


def check_attendance(students, first_name, last_name):
    for student in students:
        if student.first_name == first_name and student.last_name == last_name:
            return True
    return False


# If you would like, you may implement the Student class as
# described and use it to test your code. This is not
# necessary to complete the problem, but it may help you
# debug. If you create a Student class, all you need is
# a constructor that assigns values to two attributes:
# self.first_name and self.last_name.
