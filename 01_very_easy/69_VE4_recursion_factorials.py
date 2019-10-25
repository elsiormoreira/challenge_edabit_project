"""
Write a function that calculates the factorial of a number recursively.

Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1

"""

# my solution
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

# function test
fact(3)