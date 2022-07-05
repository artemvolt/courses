import unittest
import sys

from courses.first.bi_directional_list.BiDirectionalList import LinkedList2, Node

sys.path.append('/var/www/courses')


class LinkedListTest(unittest.TestCase):
    def test_find(self):
        list = LinkedList2()
        self.assertIsNone(list.find(5))

        will_add = Node(5)
        list.add_in_tail(will_add)
        found = list.find(5)
        self.assertIsNotNone(found)
        self.assertEqual(found, will_add)

        list.add_in_tail(Node(10))
        found = list.find(5)
        self.assertIsNotNone(found)
        self.assertEqual(5, found.value)

    def test_find_all(self):
        list = LinkedList2()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(10))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(4))
        list.add_in_tail(Node(5))

        self.assertEqual(0, len(list.find_all(11)))
        self.assertEqual(1, len(list.find_all(10)))
        self.assertEqual(2, len(list.find_all(5)))

