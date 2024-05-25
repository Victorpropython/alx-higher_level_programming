#!/usr/bin/python3
"""Define unittest for base.py.

unittest classes:
	TestBase_instantiation - line 

"""
import os 
import unittest
from models.base import base


class TestBase_instantiation(unittest.TestCase):
	"""Unittest for testing Instantiation of the Base class"""

	def test_no_arg(self):
		"""Test the number of id provided"""
		b1 = Base()
		b2 = Base()
		self.assertEqual(b1.id,b2.id - 1)
	
	def test_three_bases(self):
		b1 = Base()
		b2 = Base()
		b3 = Base()
		self.assertEqual(b1.id, b3.id - 2)
	
	def test_None_id(self)
		b1 = Base(None)
		b2 = Base(None)
		self.assertEqual(b1.id, b2.id - 1)

	def test_unique_id(self)
		self.assertEqual(12, Base(12).id)
	
	def test_nb_instances_after_unique_id(self)
		b1 = Base()
		b2 = Base()
		b3 = Base()
		self.assertEqual(b1.id, b3.id - 1)


if __init__ = "__main__":
	unittest.main()