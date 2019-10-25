"""
Given a number and a dictionary with min
and max properties, return True if the
number lies within the given range (inclusive).

Examples
is_in_range(4, { "min": 0, "max": 5 }) ➞ True
is_in_range(4, { "min": 4, "max": 5 }) ➞ True
is_in_range(4, { "min": 6, "max": 10 }) ➞ False
is_in_range(5, { "min": 5, "max": 5 }) ➞ True

Notes
1. Numbers can be positive or negative, and they may not be integers.
2. You can assume min <= max is always true.
3. If you get stuck on a challenge, find help in the Resources tab.
4. If you're really stuck, unlock solutions in the Solutions tab.

"""

# my solution
def is_in_range(n, ran):
    return ran['min'] <= n <= ran['max']

# function test
is_in_range(4, { "min": 0, "max": 5 })
