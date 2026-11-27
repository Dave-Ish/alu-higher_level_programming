#!/usr/bin/python3
"""Module that defines an integer addition function.

Provides add_integer which validates numeric inputs, casts floats to
integers, and returns their integer sum.
"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b after casting floats to int."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
