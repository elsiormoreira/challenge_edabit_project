"""
You are given 2 out of 3 of the angles in a triangle,
in degrees. Write a function that classifies the
missing angle as either "acute", "right", or "obtuse"
based on its degrees.

- An ACUTE angle is one smaller than 90 degrees.
- A RIGHT angle is one that is exactly 90 degrees.
- An OBTUSE angle is one greater than 90 degrees (but smaller than 180 degrees).

For example: missing_angle(11, 20) should return
"obtuse", since the missing angle would be 149
degrees, which makes it obtuse.

Notes
The sum of angles of any triangle is always 180 degrees.

"""

def miss_angle(ang1, ang2):
    if 180 - ang1 - ang2 == 90:
        return 'right'
    elif 180 - ang1 - ang2 > 90:
        return 'obtuse'
    else:
        return 'acute'
