#!/usr/bin/python3
"""Testing Base.py"""
import unittest
from models.square import Square
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """Test Cases"""

    def test_square_creation(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s2, Base)
        self.assertIsInstance(s3, Base)

    def test_square_validation(self):
        with self.assertRaises(TypeError):
            Square("1")
            Square(1, "2")
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(-1)
            Square(1, -2)
            Square(1, 2, -3)

    def test_square_str(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")

    def test_square_display(self):
        s1 = Square(2, 3, 4)
        s1.display()

    def test_square_update(self):
        s1 = Square(1, 2, 3, 4)
        s1.update(5, 6, 7, 8)
        self.assertEqual(str(s1), "[Square] (5) 7/8 - 6")
        s1.update(9, 10)
        self.assertEqual(str(s1), "[Square] (9) 7/8 - 10")
        s1.update(id=11)
        self.assertEqual(str(s1), "[Square] (11) 7/8 - 10")
        s1.update(y=12, x=13, size=14)
        self.assertEqual(str(s1), "[Square] (11) 13/12 - 14")

    def test_square_create(self):
        s1 = Square.create(**{'id': 1, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_square_save_and_load_from_file(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))
        os.remove("Square.json")

    def test_create_square_with_string_size(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_create_square_with_string_x(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_to_dictionary(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_create_square_with_x_and_y(self):
        s1 = Square(1, 2, 3, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

if __name__ == "__main__":
    unittest.main()
