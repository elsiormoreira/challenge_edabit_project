"""
You hired three programmers and you (hopefully) pay them. Create a function
that takes three numbers (the hourly wage of each programmer) and returns the
difference between the highest-paid programmer and the lowest-paid.
"""

def programmers(n1, n2, n3):
    return max(n1, n2, n3) - min(n1, n2, n3)
