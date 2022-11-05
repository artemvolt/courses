import unittest
import sys

from courses.first.queue.Queue import Queue

sys.path.append('/var/www/courses')


class QueueTest(unittest.TestCase):
    def test_add(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(1, queue.stack[0])
        queue.enqueue(2)
        self.assertEqual(1, queue.stack[0])
        self.assertEqual(2, queue.stack[1])

    def test_dequeue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())
        queue.enqueue(1)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(0, queue.size())

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(0, queue.size())

    def test_size(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(1, queue.size())
        queue.enqueue(2)
        self.assertEqual(2, queue.size())
        queue.enqueue(3)
        self.assertEqual(3, queue.size())

    def test_rotate(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.rotate(1)
        self.assertEqual(2, queue.stack[0])
        self.assertEqual(3, queue.stack[1])
        self.assertEqual(1, queue.stack[2])

        queue.rotate(2)
        self.assertEqual(1, queue.stack[0])
        self.assertEqual(2, queue.stack[1])
        self.assertEqual(3, queue.stack[2])

        queue = Queue()
        for k in range(1, 10):
            queue.enqueue(k)

        queue.rotate(5)

        self.assertEqual(6, queue.stack[0])
        self.assertEqual(7, queue.stack[1])
        self.assertEqual(8, queue.stack[2])
        self.assertEqual(9, queue.stack[3])
        self.assertEqual(1, queue.stack[4])
        self.assertEqual(2, queue.stack[5])
        self.assertEqual(3, queue.stack[6])

