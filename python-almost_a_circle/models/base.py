#!/usr/bin/python3
"""Module that defines the Base class for geometry models.

Manages instance IDs and provides static and class methods for JSON
serialization, deserialization, file persistence, and instance creation.
"""
import json
import os


class Base:
    """Base class for all geometry models in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from <Class name>.json."""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]
