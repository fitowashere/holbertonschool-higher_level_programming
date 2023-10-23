#!/usr/bin/python3
"""base module"""


# models/base.py

class Base:
    """
    This is the base class for your models.
    """

    # Private class attribute __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.
        """
        # Check if id is provided
        if id is not None:
            # Assign the provided id to the public instance attribute id
            self.id = id
        else:
            # Increment __nb_objects and
            # assign it to the public instance attribute id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
