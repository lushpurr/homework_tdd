import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_1_3_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(1, 3))

    def test_compare_3_3_returns_numbers_are_equal(self):
        self.assertEqual("The numbers are equal", compare(3, 3))