"""
You're given a string of words. You need to find
the word "Nemo", and return a string like this:
"I found Nemo at [the order of the word you find nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".

Examples
find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"
find_nemo("Nemo is me") ➞ "I found Nemo at 1!"
find_nemo("I Nemo am") ➞ "I found Nemo at 2!"

Notes
1. ! , ? . are always seperated from the last word.
2. Nemo will always look like "Nemo", not like "NeMo", and other capital premutations.
3. Nemo's, or anything that says Nemo, with something behind it, does not count as "Finding Nemo"!
4. If there are more "Nemo's" in the sentance, only return for the first one.

"""

# my solution
def find_nemo(string):
    string = string.split()
    if 'Nemo' in string:
        order = string.index('Nemo') + 1
        return f"I found Nemo at {order} position!"
    else:
        return "I can't find Nemo :("

# function test
find_nemo("I am finding Nemo !")
find_nemo("I Nemo am")
find_nemo("There is no name in that text.")
