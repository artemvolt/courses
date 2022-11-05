import unittest
import sys

from courses.first.stack.Stack import Stack

sys.path.append('/var/www/courses')


class StackTest(unittest.TestCase):
    def test_size(self):
        stack = Stack()
        self.assertEqual(0, stack.size())
        stack.push(1)
        self.assertEqual(1, stack.size())
        stack.push(2)
        self.assertEqual(2, stack.size())

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.size())
        self.assertEqual(1, stack.stack[0])

        stack.push(2)
        self.assertEqual(2, stack.size())
        self.assertEqual(2, stack.stack[0])
        self.assertEqual(1, stack.stack[1])

        stack.push(3)
        self.assertEqual(3, stack.size())
        self.assertEqual(3, stack.stack[0])
        self.assertEqual(2, stack.stack[1])
        self.assertEqual(1, stack.stack[2])

    def test_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())
        stack.push(1)
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, stack.size())
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, stack.pop())
        self.assertEqual(2, stack.size())

        self.assertEqual(3, stack.pop())
        self.assertEqual(1, stack.size())

        self.assertEqual(2, stack.pop())
        self.assertEqual(0, stack.size())

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertEqual(1, stack.size())
        stack.push(2)
        self.assertEqual(2, stack.peek())
        self.assertEqual(2, stack.size())
