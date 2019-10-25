"""
Write a function that recursively finds
the sum of the first n natural numbers.

Examples
sum_numbers(5) ➞ 15 (1 + 2 + 3 + 4 + 5 = 15)
sum_numbers(1) ➞ 1
sum_numbers(12) ➞ 78

"""

def rec_sum(num):
    total_sum = 0
    for i in range(1, num + 1):
        total_sum = total_sum + i
    return total_sum


rec_sum(12)
