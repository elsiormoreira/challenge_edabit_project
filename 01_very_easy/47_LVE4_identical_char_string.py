"""
Write a function that returns True if all
characters in a string are identical and
False otherwise.

Examples
is_identical("aaaaaa") ➞ True
is_identical("aabaaa") ➞ False
is_identical("ccccca") ➞ False
is_identical("kk") ➞ True

"""

def is_identical(string):
    return len(set(string)) == 1
