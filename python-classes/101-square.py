#!/usr/bin/python3
"""This module contains a square class"""


class Square:
    """A class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square object with a given size and position.

        Parameters:
            size (int): The size of the square, defaults to 0.
            position (tuple): A tuple of 2 positive integers representing
                              the position of the square, defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # using its position."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Overrides the default behavior when using print() with a Square object.

        Returns:
            A string representation of the square, ready to be printed.
        """
        from io import StringIO
        buffer = StringIO()
        print(self.my_print(), file=buffer)
        return buffer.getvalue()
