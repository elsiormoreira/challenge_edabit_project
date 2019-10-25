"""
Create a function that takes a list of
numbers and returns the sum of its cubes.

Examples
sum_of_cubes([1, 5, 9]) ➞ 855 (1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855)
sum_of_cubes([3, 4, 5]) ➞ 216
sum_of_cubes([2]) ➞ 8
sum_of_cubes([]) ➞ 0

Notes
If given an empty list, return 0.

"""

def cube_sum(num):
    total_sum = 0
    for i in range(0, len(num)):
        total_sum = total_sum + num[i] ** 3
    return total_sum

cube_sum([2, 2, 1])