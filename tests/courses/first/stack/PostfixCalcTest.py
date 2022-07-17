import sys
import unittest

from courses.first.stack.PostfixCalc import postfix_calc

sys.path.append('/var/www/courses')


class PostfixCalcTest(unittest.TestCase):
    def test_size(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(9, postfix_calc("1 + 2 * 3 ="))

        with self.assertRaises(AttributeError):
            self.assertEqual(9, postfix_calc(""))

        self.assertEqual(9, postfix_calc("1 2 + 3 * ="))
        self.assertEqual(59, postfix_calc("8 2 + 5 * 9 + ="))
        self.assertIsNone(postfix_calc("8 2 + 5 * 9 +"))
