"""
You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
Return the total number of legs on your farm.
"""

def animals(chickens, cows, pigs):
    return chickens * 2 + (cows + pigs) * 4
