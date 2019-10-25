"""
Create a function that takes a number as an argument and returns "even" for
even numbers and "odd" for odd numbers.

Notes:
1.Don't forget to return the result.
2.Input will always be a valid integer.
3.Expect negative integers (whole numbers).
4.Tests are case sensitive (return "even" or "odd" in lowercase).
"""

def even_odd(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'
