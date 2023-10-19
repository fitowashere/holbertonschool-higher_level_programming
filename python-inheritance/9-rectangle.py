#!/usr/bin/python3
"""
This module have a class called Rectangle that
is a child of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a child class from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Function that validates the weight & height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        print(str(self))
