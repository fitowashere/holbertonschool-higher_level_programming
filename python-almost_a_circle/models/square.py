#!/usr/bin/python3
"""square module"""


# models/square.py
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class.
        """
        super().__init__(size, size, x, y, id)
        # Call the constructor of the super class
        # (Rectangle) to handle id, x, y, width, and height

    # Getter and setter methods for size
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    # The __str__ method is overridden
    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance
        """
        if args:
            # If args exist, use them and skip **kwargs
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            # Use **kwargs to update attributes
            for key, value in kwargs.items():
                setattr(self, key, value)
