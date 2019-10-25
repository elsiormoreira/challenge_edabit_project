"""
Zip codes consist of 5 consecutive digits.
Given a string, write a function to determine
whether the input is a valid zip code.

Examples
is_valid("59001") ➞ True
is_valid("853a7") ➞ False
is_valid("732 32") ➞ False

Notes
Valid zip codes should not be any spaces between the digits.

"""

# my solution
def is_valid(zip_code):
    return zip_code.isdigit()

# function solution
is_valid("732 32")
