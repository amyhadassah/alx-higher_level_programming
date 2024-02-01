#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute initialized to #

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1  # Increment the number of instances
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle.
        Represents the rectangle with the character(s) stored in print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = [str(self.print_symbol) * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation of the rectangle.
        This allows recreation of a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted
        and decrement the number_of_instances.
        """
        type(self).number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        Returns:
            The bigger rectangle, or rect_1 if both have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.
        Args:
            size (int): The size of the new square.
        """
        return cls(size, size)
