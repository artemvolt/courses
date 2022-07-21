import unittest

from courses.first.deque.Deque import Deque


class DequeTest(unittest.TestCase):

    def test_add_front(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(1, deque.stack[0])
        deque.addFront(2)
        self.assertEqual(2, deque.stack[0])
        self.assertEqual(1, deque.stack[1])
        deque.addFront(3)
        self.assertEqual(3, deque.stack[0])
        self.assertEqual(2, deque.stack[1])
        self.assertEqual(1, deque.stack[2])

    def test_add_tail(self):
        deque = Deque()
        deque.addTail(1)
        self.assertEqual(1, deque.stack[0])
        deque.addTail(2)
        self.assertEqual(1, deque.stack[0])
        self.assertEqual(2, deque.stack[1])
        deque.addTail(3)
        self.assertEqual(3, deque.stack[2])
        self.assertEqual(2, deque.stack[1])
        self.assertEqual(1, deque.stack[0])

    def test_remove_front(self):
        deque = Deque()
        self.assertIsNone(deque.removeFront())
        deque.addFront(1)
        self.assertEqual(1, deque.removeFront())
        self.assertEqual(0, deque.size())
        deque.addFront(1)
        deque.addFront(2)
        deque.addFront(3)
        self.assertEqual(3, deque.removeFront())
        self.assertEqual(2, deque.size())

        self.assertEqual(2, deque.removeFront())
        self.assertEqual(1, deque.size())

        self.assertEqual(1, deque.removeFront())
        self.assertEqual(0, deque.size())

    def test_remove_tail(self):
        deque = Deque()
        self.assertIsNone(deque.removeTail())
        deque.addTail(1)
        self.assertEqual(1, deque.removeTail())
        self.assertEqual(0, deque.size())

        deque.addTail(1)
        deque.addTail(2)
        deque.addTail(3)
        self.assertEqual(3, deque.removeTail())
        self.assertEqual(2, deque.size())

        self.assertEqual(2, deque.removeTail())
        self.assertEqual(1, deque.size())

        self.assertEqual(1, deque.removeTail())
        self.assertEqual(0, deque.size())

    def test_size(self):
        deque = Deque()
        self.assertEqual(0, deque.size())
        deque.addFront(1)
        self.assertEqual(1, deque.size())
        deque.addTail(1)
        self.assertEqual(2, deque.size())
        deque.addTail(1)
        self.assertEqual(3, deque.size())

