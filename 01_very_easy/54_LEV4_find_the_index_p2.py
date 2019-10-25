"""
Create a function that finds the
index of a given item if the list is sorted.

Examples
search([1, 2, 3, 4], 3) ➞ 2
search([2, 4, 6, 8, 10], 8) ➞ 3
search([1, 3, 5, 7, 9], 11) ➞ -1

Notes
If the item is not present, return -1.

"""

# my solution
def find_index2(lst, item):
    if lst == sorted(lst) and item in lst:
        return lst.index(item)
    else:
        return -1

# function test
find_index2([1, 2, 3, 4], 3)
find_index2([2, 4, 6, 8, 10], 8)
find_index2([1, 3, 5, 7, 9], 11)
