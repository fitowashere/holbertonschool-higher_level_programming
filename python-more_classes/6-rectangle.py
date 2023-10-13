#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """A class used to represent a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the Rectangle made up of '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """String representation that can be used to recreate the object."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a farewell message when the Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
