"""
Imagine a messaging device with only one button.
For the letter A, you press the button one time,
for E, you press it five times, for G, it's
pressed seven times, etc, etc.

Write a function that takes a string (the message)
and returns the total number of times the button
is pressed.

Examples
how_many_times("abde") ➞ 12
how_many_times("azy") ➞ 52
how_many_times("qudusayo") ➞ 123

Notes
Ignore spaces.

"""

# my solution
def how_many_times(msg):
    count = 0
    for i in msg:
        count = count + ord(i) - 96
    return count

# best solution
def how_many_times1(msg):
    return sum(ord(i) - 96 for i in msg)

# function test
how_many_times("abde")