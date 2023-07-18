#!/usr/bin/python3
"""Testing Base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Cases"""

    def test_base_creation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_with_id(self):
        b3 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_base_with_id(self):
        b5 = Base()
        b6 = Base()
        self.assertEqual(b6.id, b5.id + 1)

    def test_base_with_id_increment(self):
        b1 = Base(12)
        b2 = Base(1)
        self.assertEqual(b1.id + b2.id, 13)


if __name__ == "__main__":
    unittest.main()
