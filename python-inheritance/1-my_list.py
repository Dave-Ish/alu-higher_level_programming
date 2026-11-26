#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """Represents a custom list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list elements sorted in ascending order."""
        print(sorted(self))
