#!/usr/bin/python3
"""Unit tests for the Square class in models/square.py."""
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square instantiation, validation, and persistence."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Removes Square.json if created during tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_init_and_size(self):
        """Tests Square constructors with 1 to 4 positional arguments."""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s2 = Square(1, 2)
        self.assertEqual((s2.size, s2.x), (1, 2))
        s3 = Square(1, 2, 3)
        self.assertEqual((s3.size, s3.x, s3.y), (1, 2, 3))
        s4 = Square(1, 2, 3, 4)
        self.assertEqual((s4.size, s4.x, s4.y, s4.id), (1, 2, 3, 4))
        self.assertEqual(str(s4), "[Square] (4) 2/3 - 1")

    def test_validation_type_and_value_errors(self):
        """Tests TypeError and ValueError cases for Square arguments."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_update_and_to_dictionary(self):
        """Tests Square update(*args, **kwargs) and to_dictionary()."""
        s = Square(5, 0, 0, 1)
        s.update()
        s.update(89)
        s.update(89, 1)
        s.update(89, 1, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        s.update(**{"id": 89})
        s.update(**{"id": 89, "size": 1})
        s.update(**{"id": 89, "size": 1, "x": 2})
        s.update(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        expected = {"id": 89, "size": 1, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create_square(self):
        """Tests Square.create with incremental keyword dictionaries."""
        s1 = Square.create(**{"id": 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(s2.size, 1)
        s3 = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(s3.x, 2)
        s4 = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(s4), "[Square] (89) 2/3 - 1")

    def test_save_and_load_square(self):
        """Tests Square.save_to_file and Square.load_from_file."""
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(1)])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].size, 1)


if __name__ == "__main__":
    unittest.main()
