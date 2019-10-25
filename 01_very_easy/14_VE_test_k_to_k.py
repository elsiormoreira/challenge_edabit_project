"""
Write a function that returns True if k^k == n for input (n, k). The ^ operator
refers to exponentiation operation, not the bitwise XOR operation.
"""

def k_to_k(k, n):
    return k ** k == n
