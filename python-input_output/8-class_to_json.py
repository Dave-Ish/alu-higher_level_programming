#!/usr/bin/python3
"""Module that defines a function returning a class instance dictionary."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of obj."""
    return obj.__dict__
