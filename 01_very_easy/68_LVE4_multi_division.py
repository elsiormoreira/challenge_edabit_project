"""
Create a function, that will for a given a, b, c,
do the following: Add a to itself b times and
check if the result is divisible by c.

Examples
abcmath(42, 5, 10) ➞ False
# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10

abcmath(5, 2, 1) ➞ True

abcmath(1, 2, 3) ➞ False

Notes
In the first step of the function, a doesn't always refer to the original a.
"if the result is divisible by c", means that if you divide the result and c, you will get an integer (5, and not 4.5314).

"""

# my solution
def math_check(a, b, c):
    for n in range(b):
        a += a
    if a % c == 0:
        return True
    else:
        return False


# function test
math_check(132, 70, 3)
