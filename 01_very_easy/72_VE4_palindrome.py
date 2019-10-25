"""
A palindrome is a word that is identical
forward and backwards. Given a word, create
a function that checks whether it is a palindrome.

Examples
is_palindrome("mom") ➞ True
is_palindrome("scary") ➞ False
is_palindrome("reviver") ➞ True
is_palindrome("stressed") ➞ False

Notes
All test input is lower cased.

"""

# my solution
def is_palindrome(txt):
    return txt == txt[::-1]

