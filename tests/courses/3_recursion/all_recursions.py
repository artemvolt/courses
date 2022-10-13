import unittest
import sys

sys.path.append('/var/www/courses')

from courses.third_recursion.first_to_a_power import number_to_a_power
from courses.third_recursion.second_sum_nums_of_number import sum_of_the_numbers_of_number


class AllRecursions(unittest.TestCase):

    def test_number_to_a_power(self):
        self.assertEqual(1, number_to_a_power(2, 0))
        self.assertEqual(2, number_to_a_power(2, 1))
        self.assertEqual(4, number_to_a_power(2, 2))
        self.assertEqual(8, number_to_a_power(2, 3))
        self.assertEqual(16, number_to_a_power(2, 4))

    def test_sum_of_the_numbers_of_number(self):
        self.assertEqual(0, sum_of_the_numbers_of_number(0))
        self.assertEqual(1, sum_of_the_numbers_of_number(1))
        self.assertEqual(3, sum_of_the_numbers_of_number(12))
        self.assertEqual(6, sum_of_the_numbers_of_number(123))
        self.assertEqual(10, sum_of_the_numbers_of_number(1234))
        self.assertEqual(15, sum_of_the_numbers_of_number(12345))
