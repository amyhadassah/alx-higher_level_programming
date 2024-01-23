#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        size (number): The size of the square, must be a number (float or integer) and >= 0.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (number): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (number): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the behavior for the equality operator ==."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the behavior for the inequality operator !=."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the behavior for the greater than operator >."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the behavior for the greater than or equal operator >=."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define the behavior for the less than operator <."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the behavior for the less than or equal operator <=."""
        return self.area() <= other.area()

