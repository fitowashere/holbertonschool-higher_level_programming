#!/usr/bin/python3
"""base module"""


import json
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

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        # Use the update method to apply values from the dictionary
        return dummy_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dictionaries)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
