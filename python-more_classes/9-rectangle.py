#!/usr/bin/python3
"""This module have a class that defines a rectangle"""


class Rectangle:
    """A class used to represent a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle, ensuring it is a positive integer."""
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
        """Rectangle, ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """The perimeter of the Rectangle, or 0 if either dimension is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Representation of the Rectangle made of the print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n") * self.__height

    def __repr__(self):
        """Rectangle that can be used to recreate the same object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Decrement the number_of_instances when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Rectangle, or rect_1 if they are equal, based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with equal width and height."""
        return cls(size, size)
