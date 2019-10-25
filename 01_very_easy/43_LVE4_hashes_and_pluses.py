"""
Create a function that returns the number
of hashes and pluses in a string.

Notes
It should return [0, 0] for an empty string.

Examples
hash_plus_count("###+") ➞ [3, 1]
hash_plus_count("##+++#") ➞ [3, 3]
hash_plus_count("#+++#+#++#") ➞ [4, 6]
hash_plus_count("") ➞ [0, 0]

"""

def hash_plus(string):
    return [string.count('#'), string.count('+')]
