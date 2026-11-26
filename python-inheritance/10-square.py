#!/usr/bin/python3
"""Module that defines a Square class inheriting Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle inheritance."""

    def __init__(self, size):
        """Initializes a Square instance with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
