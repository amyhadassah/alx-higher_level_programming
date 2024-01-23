#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class that defines a square by its size.
    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
