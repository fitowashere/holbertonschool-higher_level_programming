#!/usr/bin/python3
"""Module to create a class from JSON file"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
