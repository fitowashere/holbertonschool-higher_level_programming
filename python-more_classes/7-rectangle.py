#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """A magical Rectangle class."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Rectangle with special width, height, and a magic symbol!"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Find out how wide the rectangle is."""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle's width is a positive number, or say it's not allowed!"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Find out how tall the rectangle is."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height is a positive number, or say it's not allowed!"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Find out how big the rectangle is on the inside."""
        return self.width * self.height

    def perimeter(self):
        """The edge of the rectangle and find out how long it is."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Make a picture of the rectangle using its magic symbol!"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """A magic spell to make a rectangle just like this one!"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Say 'Bye rectangle...' when the rectangle goes away."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
