#!/usr/bin/python3
"""rectanle module"""


# models/rectangle.py
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.
        """
        super().__init__(id)
        # Call the constructor of the class Base to handle id assignment
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter methods for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer")
        self.__width = value

    # Getter and setter methods for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Height must be a positive integer")
        self.__height = value

    # Getter and setter methods for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        self.__x = value

    # Getter and setter methods for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        self.__y = value
