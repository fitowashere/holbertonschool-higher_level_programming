#!/usr/bin/python3
"""This module contains a square class"""


class Square:
    """Class to represent a square."""

    def __init__(self, size=0):
        """
        Initializes the Square instance with the provided size.

        Parameters:
        - size (int): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validations.

        Parameters:
        - value (int): The new size of the square's sides.

        Raises:
        - TypeError: If the provided size is not an integer.
        - ValueError: If the provided size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
