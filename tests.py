# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############


# For unittesting
import unittest

# Loading all the modules
from array_compaction.array_compaction import array_compaction
from array_rotation.array_rotation import rotate
from lcm.lcm import calculate_lcm
from characters_string.characters_string import unique_elements_non_linear, unique_elements_linear

class ArrayCompactionTest(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(array_compaction([1,2,2,3]), [1,2,3])

class ArrayRotationTest(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(rotate([1, 2, 3, 4, 5, 6], 2), [5, 6, 1, 2, 3, 4])

class LCMTest(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(calculate_lcm([1,2,3]),6)

class CharactersString(unittest.TestCase):
	def test_basic_non_linear(self):
		self.assertEqual(unique_elements_non_linear([1,2,3],[3,2]), [2,3])

	def test_basic_linear(self):
		self.assertEqual(unique_elements_linear([1,2,3],[3,2]), [2,3])

if __name__ == '__main__':
    unittest.main()