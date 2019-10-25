"""
Create a function that gets an object arguments with height, width and length
of a box and returns the volume of the box.
"""

def vol(width, length, heigth):  # input as numbers
    return width * length * heigth

def volume_of_box(sizes):  # input as dictionary
    result = 1
    for i in sizes.values():
        result = result * i
    return result
