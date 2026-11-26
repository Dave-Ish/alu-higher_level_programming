#!/usr/bin/python3
"""Module that defines a function to check strict subclass inheritance."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a strict subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
