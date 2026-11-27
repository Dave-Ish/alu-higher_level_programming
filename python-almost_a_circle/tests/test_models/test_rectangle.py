#!/usr/bin/python3
"""Unit tests for the Rectangle class in models/rectangle.py."""
import io
import os
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle attributes, validation, and methods."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Removes Rectangle.json if created during tests."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_init_and_getters(self):
        """Tests valid Rectangle instantiation and getters."""
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))
        r2 = Rectangle(1, 2, 3)
        self.assertEqual((r2.width, r2.height, r2.x), (1, 2, 3))
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual((r3.width, r3.height, r3.x, r3.y), (1, 2, 3, 4))
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_validation_type_errors(self):
        """Tests TypeError for non-integer width, height, x, and y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_validation_value_errors(self):
        """Tests ValueError for invalid ranges of width, height, x, and y."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area_and_str(self):
        """Tests area() and __str__() output."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.area(), 24)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """Tests display() without x and y offsets."""
        r = Rectangle(2, 2)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Tests display() without y offset."""
        r = Rectangle(2, 2, 2)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "  ##\n  ##\n")

    def test_display(self):
        """Tests display() with both x and y offsets."""
        r = Rectangle(2, 3, 2, 1)
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n  ##\n  ##\n  ##\n")

    def test_update_args_and_kwargs(self):
        """Tests update() with positional *args and keyword **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        r.update(89)
        r.update(89, 1)
        r.update(89, 1, 2)
        r.update(89, 1, 2, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        r.update(**{"id": 89})
        r.update(**{"id": 89, "width": 1})
        r.update(**{"id": 89, "width": 1, "height": 2})
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3})
        r.update(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_to_dictionary(self):
        """Tests to_dictionary() output."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_create_rectangle(self):
        """Tests Rectangle.create with incremental keyword dictionaries."""
        r1 = Rectangle.create(**{"id": 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r2.width, 1)
        r3 = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r3.height, 2)
        r4 = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(r4.x, 3)
        r5 = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        )
        self.assertEqual(str(r5), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_and_load_rectangle(self):
        """Tests Rectangle.save_to_file and Rectangle.load_from_file."""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual((loaded[0].width, loaded[0].height), (1, 2))


if __name__ == "__main__":
    unittest.main()
