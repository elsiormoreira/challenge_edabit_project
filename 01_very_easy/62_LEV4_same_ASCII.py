"""
Return True if the sum of ASCII values of
the first string is same as the sum of
ASCII values of the second string, otherwise
return False.

Examples
same_ascii("a", "a") ➞ True
same_ascii("AA", "B@") ➞ True
same_ascii("EdAbIt", "EDABIT") ➞ False

"""

# my solution
def same_ascii(a, b):
    return sum(ord(i) for i in a) == sum(ord(n) for n in b)

# function test
same_ascii("EdAbIt", "EDABIT")
