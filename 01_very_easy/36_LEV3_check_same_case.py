"""
Create a function that returns True if an
input string contains only uppercase or
only lowercase letters.

"""

def same_case(txt):
    return txt.isupper() or txt.islower()
