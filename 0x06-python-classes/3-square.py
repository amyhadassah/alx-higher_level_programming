#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        size (int): The size of the square, must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
