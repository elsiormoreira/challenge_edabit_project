"""
Write a function that returns True if two
arrays have the same number of unique
elements, and false otherwise.

Examples
same([1, 3, 4, 4, 4], [2, 5, 7]) ➞ True
same([9, 8, 7, 6], [4, 4, 3, 1]) ➞ False
same([2], [3, 3, 3, 3, 3]) ➞ True

"""

def same_num(arr1, arr2):
    return len(set(arr1)) == len(set(arr2))
