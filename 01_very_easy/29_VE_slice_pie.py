"""
Create a function that determines whether or not it's possible to split a
pie fairly given these three parameters:

1. Total number of slices.
2. Number of recipients.
3. How many slices each person gets.

Notes:
- Return (trivially) True if there are zero people.
- It's fine not to use the entire pie.
- All test parameters are integers.
"""

def split_pie(tot_slice, num_recip, slices_per):
    return num_recip * slices_per <= tot_slice
