#!/usr/bin/python3
"""adds attribute to object"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible,
    otherwise raises a TypeError.
    """
    if hasattr(obj, '__slots__') or not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
