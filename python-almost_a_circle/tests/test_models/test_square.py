#!/usr/bin/python3
"""Unit tests for the Square class in models/square.py."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square inheritance, size property, and methods."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_init_and_size(self):
        """Tests Square instantiation, size getter/setter, and validation."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.size = 8
        self.assertEqual(s.size, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_update_and_to_dictionary(self):
        """Tests Square update(*args, **kwargs) and to_dictionary()."""
        s = Square(5, 0, 0, 1)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")
        s.update(size=7, y=1, id=89)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 7")
        expected = {"id": 89, "size": 7, "x": 3, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
