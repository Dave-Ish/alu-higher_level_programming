#!/usr/bin/python3
"""Module that defines a Square class that can print itself."""


class Square:
    """Represents a square that can compute area and print to stdout."""
    def __init__(self, size=0):
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

    def my_print(self):
        """Prints the square in stdout using the character #."""
        if self.__size == 0:
            print("")
        return
        for _ in range(self.__size):
            print("#" * self.__size)
