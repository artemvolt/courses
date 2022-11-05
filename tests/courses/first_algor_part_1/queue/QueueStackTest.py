import sys
import unittest

from courses.first.queue.QueueStack import QueueStack

sys.path.append('/var/www/courses')


class QueueStackTest(unittest.TestCase):
    def test_add(self):
        queue = QueueStack()
        queue.enqueue(1)
        self.assertEqual(1, queue.stack.peek())
        queue.enqueue(2)
        self.assertEqual(1, queue.stack.pop())
        self.assertEqual(2, queue.stack.pop())

    def test_dequeue(self):
        queue = QueueStack()
        self.assertIsNone(queue.dequeue())
        queue.enqueue(1)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(0, queue.size())
        #
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(3, queue.size())
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(0, queue.size())

    def test_size(self):
        queue = QueueStack()
        queue.enqueue(1)
        self.assertEqual(1, queue.size())
        queue.enqueue(2)
        self.assertEqual(2, queue.size())
        queue.enqueue(3)
        self.assertEqual(3, queue.size())

    def test_rotate(self):
        queue = QueueStack()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.rotate(1)
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(1, queue.dequeue())

        queue = QueueStack()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.rotate(2)
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())

        queue = QueueStack()
        for k in range(1, 10):
            queue.enqueue(k)

        queue.rotate(5)

        self.assertEqual(6, queue.dequeue())
        self.assertEqual(7, queue.dequeue())
        self.assertEqual(8, queue.dequeue())
        self.assertEqual(9, queue.dequeue())
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

