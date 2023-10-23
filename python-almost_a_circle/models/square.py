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

    # The __str__ method is overridden
    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
