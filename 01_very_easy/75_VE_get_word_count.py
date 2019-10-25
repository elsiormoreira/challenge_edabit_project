"""
Create a function that takes a string
and returns the word count. The string
will be a sentence.

Examples
count_words("Just an example here move along") ➞ 6
count_words("This is a test") ➞ 4
count_words("What an easy task, right") ➞ 5

Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""

# my solution
def count_words(txt):
    return len(txt.split(' '))

# function test
count_words("What an easy task, right")