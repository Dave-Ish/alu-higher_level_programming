#!/usr/bin/python3
"""Module that defines the Square class inheriting from Rectangle.

Provides a specialized square model sharing Rectangle validation and
rendering while exposing a unified size property.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance with validated size and offsets."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets width and height to value using Rectangle validation."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the formatted string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assigns positional or keyword arguments to Square attributes."""
        attrs = ("id", "size", "x", "y")
        if args and len(args) > 0:
            for idx, val in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], val)
        elif kwargs:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
