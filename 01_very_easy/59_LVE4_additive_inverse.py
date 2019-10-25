"""
A number added with its additive inverse
equals zero. Create a function that returns
a list of additive inverses.

Examples
additive_inverse([5, -7, 8, 3]) ➞ [-5, 7, -8, -3]
additive_inverse([1, 1, 1, 1, 1]) ➞ [-1, -1, -1, -1, -1]
additive_inverse([-5, -25, 35]) ➞ [5, 25, -35]

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""

def additive_inverse(lst):
    return [i * -1 for i in lst]
