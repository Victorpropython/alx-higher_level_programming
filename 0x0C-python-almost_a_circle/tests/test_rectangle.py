#!/usr/bin/python3
#test_rectangle.py
#Victor chibuike
"""Defines unittest for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 
    TestRectangle_width - line
    TestRectangle_height - line
    TestRectangle_x - line
    TestRectangle_y - line
    TestRectangle_order_of_instantiation - line
    TestRectangle_area - line
    TestRectangle_update_args - line
    TestRectangle_update_kwargs - line
    TestRectangle_to_dictionary - line
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unitest to test instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstances(Rectangle(10,2), Base)

    def test_no_args(self):
        r = Rectangle
        with self.assertRaises(TypeError):
            r()
    
    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id -1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id -1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)
