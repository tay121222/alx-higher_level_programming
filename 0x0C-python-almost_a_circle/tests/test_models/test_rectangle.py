#!/usr/bin/python3
"""Contains Testcases for Rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import os


class TestRectangle(unittest.TestCase):
    """Testcases for Rectangle"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Rectangle_creation(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rec_with_id(self):
        r2 = Rectangle(8, 4, 2, 3, 100)
        self.assertEqual(r2.width, 8)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 100)

    def test_getters_and_setters(self):
        r3 = Rectangle(6, 3)
        r3.width = 12
        r3.height = 7
        r3.x = 4
        r3.y = 2
        self.assertEqual(r3.width, 12)
        self.assertEqual(r3.height, 7)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 2)

    def test_rectangle_creation2(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r1, Base)
        self.assertIsInstance(r2, Base)
        self.assertIsInstance(r3, Base)

    def test_rectangle_area(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

    def test_rectangle_str(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (1) 3/4 - 1/2")

    def test_rectangle_display(self):
        r1 = Rectangle(2, 3)
        r1.display()

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.to_dictionary(), {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_rectangle_update(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(6, 7, 8, 9, 10)
        self.assertEqual(str(r1), "[Rectangle] (6) 9/10 - 7/8")
        r1.update(11, 12, 13)
        self.assertEqual(str(r1), "[Rectangle] (11) 9/10 - 12/13")
        r1.update(id=14)
        self.assertEqual(str(r1), "[Rectangle] (14) 9/10 - 12/13")
        r1.update(y=15, x=16, width=17, height=18)
        self.assertEqual(str(r1), "[Rectangle] (14) 16/15 - 17/18")

    def test_rectangle_create(self):
        r1 = Rectangle.create(**{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")

    def test_rectangle_save_and_load_from_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(str(rectangles[0]), str(r1))
        self.assertEqual(str(rectangles[1]), str(r2))
        os.remove("Rectangle.json")

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

if __name__ == '__main__':
    unittest.main()
