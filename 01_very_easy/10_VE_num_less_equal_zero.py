"""
Create a function that takes a number as its only argument and returns
True if it's less than or equal to zero, otherwise return False.
"""

def compare(num):
    if num <= 0:
        return 'True'
    else:
        return 'False'


# other way to solve this problem
def compare(num):
    return num <= 0
