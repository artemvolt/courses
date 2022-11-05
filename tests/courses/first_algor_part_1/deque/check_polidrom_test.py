import unittest

from courses.first.deque.check_polidrom import check_palidrom


class check_palidrom_test(unittest.TestCase):

    def test_correct(self):
        self.assertFalse(check_palidrom(""))
        self.assertFalse(check_palidrom("a"))
        self.assertFalse(check_palidrom("abssb"))
        self.assertFalse(check_palidrom("qweewqq"))
        self.assertTrue(check_palidrom("abssba"))
        self.assertTrue(check_palidrom("qweewq"))
        self.assertTrue(check_palidrom("helloolleh"))


