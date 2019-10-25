"""
Write a function that takes an integer
and returns a string with the given
number of "a"s in Edabit.

Examples
how_many_times(5) ➞ "Edaaaaabit"
how_many_times(0) ➞ "Edbit"
how_many_times(12) ➞ "Edaaaaaaaaaaaabit"

"""

def edabit(n):
    return 'Ed{}bit'.format('a' * n)


edabit(12)
