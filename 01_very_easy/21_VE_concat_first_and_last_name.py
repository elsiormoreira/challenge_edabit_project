"""
Given two strings, first_name and last_name, return a single string in the
format "last, first".
"""

def concat_name1(first_name, last_name):
    return f'{last_name}, {first_name}'

def concat_name2(first_name, last_name):
    return '{}, {}'.format(last_name, first_name)
