#!/usr/bin/python3
"""Module that defines the Rectangle class inheriting from Base.

Provides validated dimensions and coordinates, area calculation, ASCII
rendering, string representation, variadic updates, and dict export.
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle with validated width, height, x, and y."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance with validated attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets and validates the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets and validates the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets and validates the x coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets and validates the y coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance using '#' with x and y offsets."""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns the formatted string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Assigns positional or keyword arguments to Rectangle attributes."""
        attrs = ("id", "width", "height", "x", "y")
        if args and len(args) > 0:
            for idx, val in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], val)
        elif kwargs:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
