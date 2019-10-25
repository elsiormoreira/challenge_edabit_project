"""
Given a list of numbers, negate all elements contained within.
"""

def negate(lst):
    for i in range(len(lst)):
        lst[i] = -lst[i]
    return lst
