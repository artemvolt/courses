import unittest
import sys

from courses.third_recursion.third_length_list import length_list

sys.path.append('/var/www/courses')

from courses.third_recursion.first_to_a_power import number_to_a_power
from courses.third_recursion.second_sum_nums_of_number import sum_of_the_numbers_of_number
from courses.third_recursion.fourth_is_palindrome import is_palindrome


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

    def test_length_list(self):
        self.assertEqual(0, length_list([]))
        self.assertEqual(1, length_list([1]))
        self.assertEqual(2, length_list([1, 2]))
        self.assertEqual(3, length_list([1, 2, 3]))

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome("a"))
        self.assertFalse(is_palindrome("abssb"))
        self.assertFalse(is_palindrome("qweewqq"))
        self.assertTrue(is_palindrome("abssba"))
        self.assertTrue(is_palindrome("qweewq"))
        self.assertTrue(is_palindrome("helloolleh"))