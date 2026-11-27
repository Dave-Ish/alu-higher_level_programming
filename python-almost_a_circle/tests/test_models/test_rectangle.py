#!/usr/bin/python3
"""Unit tests for the Rectangle class in models/rectangle.py."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle attributes, validation, and methods."""

    def setUp(self):
        """Resets __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_init_and_getters(self):
        """Tests valid Rectangle instantiation and getters."""
        r = Rectangle(10, 2, 3, 4, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 99)

    def test_validation_type_errors(self):
        """Tests TypeError for non-integer width, height, x, and y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3", 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_validation_value_errors(self):
        """Tests ValueError for invalid ranges of width, height, x, and y."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

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
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
        r.update(height=7, width=8, x=1, y=2, id=90)
        self.assertEqual(str(r), "[Rectangle] (90) 1/2 - 8/7")
        r.update(55, width=99)
        self.assertEqual(r.id, 55)
        self.assertEqual(r.width, 8)

    def test_to_dictionary(self):
        """Tests to_dictionary() output."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
