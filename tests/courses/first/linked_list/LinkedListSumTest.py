import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first.linked_list.LinkedListSum import linked_list_sum
from courses.first.linked_list.LinkedList import Node, LinkedList


class LinkedListSumTest(unittest.TestCase):

    def test_linked_list_sum(self):
        first_list = LinkedList()
        first_list.add_in_tail(Node(33))
        first_list.add_in_tail(Node(34))
        first_list.add_in_tail(Node(10))

        second_list = LinkedList()
        second_list.add_in_tail(Node(50))
        second_list.add_in_tail(Node(40))
        second_list.add_in_tail(Node(32))

        sum_list = linked_list_sum(first_list, second_list)
        self.assertEqual(3, sum_list.len())
        self.assertEqual(83, sum_list.head.value)
        self.assertEqual(74, sum_list.head.next.value)
        self.assertEqual(42, sum_list.head.next.next.value)