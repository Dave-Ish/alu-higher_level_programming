#!/usr/bin/python3
"""Module that defines a Square class capable of computing its area."""


class Square:
    """Represents a square with validated size and area calculation."""
    def init(self, size=0):
        """Initializes a new Square instance after validating size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        
    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
