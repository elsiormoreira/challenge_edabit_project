"""
Create a function that returns True if the first list can be nested inside
the second. list1 can be nested inside list2 if:

- list1's min is greater than list2's min.
- list1's max is less than list2's max.
"""

def nest(l1, l2):
    return min(l1) > min(l2) and max(l1) < max(l2)
