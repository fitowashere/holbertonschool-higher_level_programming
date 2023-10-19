#!/usr/bin/python3
"""Write a function that returns True or False"""


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
