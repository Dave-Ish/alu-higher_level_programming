#!/usr/bin/python3
"""Module that defines a Square class with property getters and setters."""


class Square:
    """Represents a square with controlled access to its size."""
    def init(self, size=0):
        """Initializes a new Square instance with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validating type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
