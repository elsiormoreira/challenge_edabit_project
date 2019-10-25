"""
Create a function that adds a string ending to each member in a list.

Examples
add_ending(["clever", "meek", "hurried", "nice"], "ly")
➞ ["cleverly", "meekly", "hurriedly", "nicely"]

add_ending(["new", "pander", "scoop"], "er")
➞ ["newer", "panderer", "scooper"]

add_ending(["bend", "sharpen", "mean"], "ing")
➞ ["bending", "sharpening", "meaning"]

Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.

"""


# my solution
def add_end(lst, char):
    final_lst = []
    for i in lst:
        final_lst.append('{}{}'.format(i, char))
    return final_lst

# best solution
def add_end(lst, char):
    return [i + char for i in lst]

# function test
add_end(["clever", "meek", "hurried", "nice"], "ly")
add_end(["new", "pander", "scoop"], "er")
add_end(["bend", "sharpen", "mean"], "ing")