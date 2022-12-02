import unittest
import sys

from courses.first_algor_part_2.five_build_balance_tree.GenerateBBSTArray import GenerateBBSTArray

sys.path.append('/var/www/courses')


class GenerateBBSTArrayTest(unittest.TestCase):

    def test_empty(self):
        result = GenerateBBSTArray([])
        self.assertEqual([], result)

    def test_one(self):
        result = GenerateBBSTArray([0])
        self.assertEqual([0], result)

        result = GenerateBBSTArray([5])
        self.assertEqual([5], result)

    def test_few(self):
        result = GenerateBBSTArray([1, 2, 3])
        self.assertEqual([2, 1, 3], result)

        result = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([4, 2, 6, 1, 3, 5, 7], result)

        result = GenerateBBSTArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], result)



