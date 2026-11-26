#!/usr/bin/python3
"""Module that defines a Square class with custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with custom [Square] string output."""

    def __init__(self, size):
        """Initializes a Square instance with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string description of the square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
