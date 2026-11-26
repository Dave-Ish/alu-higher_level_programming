#!/usr/bin/python3
"""Module that defines a full Rectangle class inheriting BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with area calculation and string output."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string description of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
