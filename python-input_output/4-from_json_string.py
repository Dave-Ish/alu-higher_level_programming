#!/usr/bin/python3
"""Module that defines a function to parse a JSON string into an object."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
