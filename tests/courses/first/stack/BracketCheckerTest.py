import unittest
import sys

from courses.first.stack.BracketChecker import bracket_check

sys.path.append('/var/www/courses')


class BracketCheckerTest(unittest.TestCase):
    def test_check(self):
        self.assertFalse(bracket_check("())("))
        self.assertFalse(bracket_check("))(("))
        self.assertFalse(bracket_check("))(("))
        self.assertFalse(bracket_check("((())"))
        self.assertTrue(bracket_check("()(())"))
        self.assertTrue(bracket_check("((())())"))

