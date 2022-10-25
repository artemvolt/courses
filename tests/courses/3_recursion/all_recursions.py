import os
import unittest
import sys
import io
from contextlib import redirect_stdout

from courses.third_recursion.third_length_list import length_list

sys.path.append('/var/www/courses')

from courses.third_recursion.first_to_a_power import number_to_a_power
from courses.third_recursion.second_sum_nums_of_number import sum_of_the_numbers_of_number
from courses.third_recursion.fourth_is_palindrome import is_palindrome
from courses.third_recursion.fifth_even_numbers import print_even_numbers
from courses.third_recursion.six_even_index import print_with_even_index
from courses.third_recursion.seven_find_second_max_number import find_second_max_number
from courses.third_recursion.eight_files import find_files_in_folders


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

    def test_print_even_numbers(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print_even_numbers([1, 2, 3, 4])
        out = f.getvalue()

        self.assertEqual("2\n4\n", out)

    def test_print_with_even_index(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print_with_even_index([1, 213, 343, 453, 877])
        out = f.getvalue()

        self.assertEqual("1\n343\n877\n", out)

    def test_find_second_max_number(self):
        self.assertEqual(None, find_second_max_number([]))
        self.assertEqual(1, find_second_max_number([1, 2]))
        self.assertEqual(3, find_second_max_number([1, 2, 4, 4, 3]))
        self.assertEqual(4, find_second_max_number([1, 2, 4, 4, 3, 5, 5]))

    def test_find_files_in_directory(self):
        files = find_files_in_folders('tests/courses/3_recursion/find_files')
        replaced = map(lambda abs_path: abs_path.replace('/var/www/tests/courses/3_recursion/', ''), files)
        replaced_to_list = list(replaced)
        self.assertEqual(5, len(replaced_to_list))
        self.assertEqual('find_files/1.txt', replaced_to_list[0])
        self.assertEqual('find_files/one/one_one/one_one_one/one_one_one.txt', replaced_to_list[1])
        self.assertEqual('find_files/three/three.txt', replaced_to_list[2])
        self.assertEqual('find_files/two/two.txt', replaced_to_list[3])
        self.assertEqual('find_files/two/two_two/two_two.txt', replaced_to_list[4])