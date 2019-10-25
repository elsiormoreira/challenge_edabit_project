"""
Create a function that checks
if the argument is an integer
or a string.

If it's an integer, return "int"
If it's a string, return "str"

Examples
int_or_string(3) ➞ "int"
int_or_string("Hello") ➞ "str"
int_or_string(8) ➞ "int"
int_or_string("Yo") ➞ "str"
int_or_string(9843532) ➞ "int"

"""

# my solution
def int_or_string(var):
    if isinstance(var, int):
        return 'int'
    else:
        return 'str'
