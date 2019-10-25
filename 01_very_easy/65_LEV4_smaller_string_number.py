"""
Create a function that returns the smaller number.

Examples
smaller_num("21", "44") ➞ "21"
smaller_num("1500", "1") ➞ "1"
smaller_num("5", "5") ➞ "5"

Notes
1. Numbers will be represented as strings, and your output should also be a string.
2. If both numbers tie, return either number.
3. Numbers will be positive.
4. Bonus: See if you can do this without converting to integers.

"""

# my solution
def smaller_num(n1, n2):
    return str(min(int(n1), int(n2)))

# best solution
def smaller_num1(n1, n2):
    return min(n1, n2)
