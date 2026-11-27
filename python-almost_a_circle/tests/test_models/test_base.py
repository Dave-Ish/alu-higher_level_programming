#!/usr/bin/python3
"""Unit tests for the Base class in models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base class functionality and JSON persistence."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up generated JSON files after each test."""
        for fname in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_auto_id(self):
        """Tests automatic sequential ID assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_explicit_id(self):
        """Tests explicit ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        """Tests serialization of list of dicts to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        res = Base.to_json_string([{"id": 12}])
        self.assertEqual(res, '[{"id": 12}]')

    def test_from_json_string(self):
        """Tests deserialization of JSON string to list of dicts."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])

    def test_save_and_load_rectangle(self):
        """Tests save_to_file and load_from_file for Rectangle."""
