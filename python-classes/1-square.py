#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initializes a new Square instance with a given size."""
        self.__size = size
