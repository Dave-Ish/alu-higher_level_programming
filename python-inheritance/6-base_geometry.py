#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Represents a base geometry object with area interface."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
