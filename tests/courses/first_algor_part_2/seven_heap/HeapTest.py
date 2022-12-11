import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first_algor_part_2.seven_pyramid.Heap import Heap


class HeapTest(unittest.TestCase):
    def test_make(self):
        heap = Heap()
        array = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(heap.HeapArray, [])
        heap.MakeHeap(array, 2)
        self.assertEqual(heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])

        _input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        heap = Heap()
        heap.MakeHeap(_input, 3)
        self.assertEqual(15, len(heap.HeapArray))
        self.assertEqual(
            [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None],
            heap.HeapArray
        )

    def test_add(self):
        heap = Heap()
        array = [None] * 15
        heap.MakeHeap(array, 3)
        heap.Add(1)
        heap.Add(2)
        heap.Add(3)
        heap.Add(4)
        heap.Add(5)
        heap.Add(6)
        heap.Add(7)
        heap.Add(8)
        heap.Add(9)
        heap.Add(11)

        self.assertEqual(
            [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None],
            heap.HeapArray
        )

    def test_get_max(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        heap = Heap()
        self.assertEqual(heap.HeapArray, [])
        heap.MakeHeap(array, 2)
        self.assertEqual(heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])
        self.assertEqual(heap.GetMax(), 7)
        self.assertEqual(heap.HeapArray, [6, 4, 5, 1, 3, 2, None])
