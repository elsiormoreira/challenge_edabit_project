"""
I'm trying to watch some lectures to
study for my next exam but I keep
getting distracted by meme compilations,
vine compilations, anime, and more
on my favorite video platform.

Your job is to help me by creating a
function that takes in a String and
checks to see if it contains the
following words or phrases: "anime",
"meme", "vine", "roasts", "Danny Devito".
If is does, return "NO!". Otherwise,
return "Safe watching!".

Examples
prevent_distractions("vines that butter my eggroll") ➞ "NO!"
prevent_distractions("Hot pictures of Danny Devito") ➞ "NO!"
prevent_distractions("How to ace BC Calculus in 5 Easy Steps") ➞ "Safe watching!"

Notes
Use the words or phrases contained above EXACTLY
(don't try to check for capitalization for any
words/phrases except for Danny Devito).
You only have to use the words mentioned.

"""

# my solution
def prevent_distractions(txt):
    list = ['anime', 'meme', 'vine', 'roasts', 'Danny Devito']
    for i in list:
        if i in txt == True:
            return 'Safe watching!'
        else:
            return 'NO!'

# functioni test
prevent_distractions("vines that butter my eggroll")
prevent_distractions("Hot pictures of Danny Devito")
prevent_distractions("How to ace BC Calculus in 5 Easy Steps")