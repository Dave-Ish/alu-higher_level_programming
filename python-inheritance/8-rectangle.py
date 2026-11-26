#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated private dimensions."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
