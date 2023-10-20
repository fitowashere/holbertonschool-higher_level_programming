#!/usr/bin/python3
"""Module convert to json"""


def class_to_json(obj):
    """ returns a dictionaty description with simple data structure"""
    return obj.__dict__
