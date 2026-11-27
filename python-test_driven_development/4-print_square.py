#!/usr/bin/python3
"""Module that defines a function to print a square using '#' characters.

Provides print_square which validates integer size >= 0 and renders
a square grid of hashes to stdout.
"""


def print_square(size):
    """Prints a square with the character # of dimension size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
