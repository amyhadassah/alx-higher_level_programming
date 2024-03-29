#!/usr/bin/python3
import math

class MagicClass:
    """A class that defines a circle with a private radius."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (int/float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
