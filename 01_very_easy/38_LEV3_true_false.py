"""
In Python, a truthy value is a value that translates
to True when evaluated in a Boolean context. All values
are truthy unless they're defined as falsy.

All falsy values are as follows: False, None, 0, [], {}, ""

Create a function that takes an argument of any data
type and returns 1 if it's truthy and 0 if it's falsy.

"""

def true_false(val):
    if bool(val) == True:
        return 1
    else:
        return 0
