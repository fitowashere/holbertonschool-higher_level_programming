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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter methods for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter methods for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter methods for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance as a grid of '#' characters.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        r = self
        return f"[Rectangle] ({r.id}) {r.x}/{r.y} - {r.width}/{r.height}"

    def update(self, *args,**kwargs):
        """
        Update the attributes of the Rectangle instance with no-keyword
        arguments in the specified order.
        """
        if args:
            # If args exist, use them and skip **kwargs
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            # Use **kwargs to update attributes
            for key, value in kwargs.items():
                setattr(self, key, value)
