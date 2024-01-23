#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """A class that defines a square by its size and position.

    Attributes:
        size (int): The size of the square, must be an integer and >= 0.
        position (tuple): The position of the square as a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character considering position."""
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
