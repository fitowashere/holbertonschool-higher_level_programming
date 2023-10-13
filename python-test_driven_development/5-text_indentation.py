#!/usr/bin/python3
"""This module will have a function that will print a text"""


def text_indentation(text):
    """
    Function that prints a text
    with 2 new lines after each
    of the chracters above.
    First we check that what its
    passed is a str, then proceed to check and print.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    
    skip_space = False
    # Add a flag to skip spaces after special characters
    for let in text:
        if skip_space and let == " ":
            continue
        elif let in ['.', '?', ':']:
            print(let, end="")
            print("\n")
            skip_space = True
            # Enable the flag after special characters
        else:
            print(let, end="")
            skip_space = False
            # Disable the flag when non-space character is encountered

