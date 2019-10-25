"""
Write a function that returns 0 if the input is 1,
and returns 1 if the input is 0.

Examples
flip(1) ➞ 0
flip(0) ➞ 1

Notes
Bonus: Do this without using any:
- conditionals or ternary operators.
- negations.
- bit operators.

"""

# my solution
def flip(a):
    if a == 1:
        return 0
    elif a == 0:
        return 1

# best solution
def flip(a):
    return 1-a

# function test
flip(1)
flip(0)