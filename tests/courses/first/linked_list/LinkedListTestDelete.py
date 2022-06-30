import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first.linked_list.LinkedList import Node, LinkedList


class LinkedListTestDelete(unittest.TestCase):
    def test_delete_one(self):
        n1 = Node(30)
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)

        linked_list.delete(n1.value)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_delete_first(self):
        n1 = Node(30)
        n2 = Node(44)
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)

        linked_list.delete(n1.value)
        self.assertEqual(n2, linked_list.head)
        self.assertEqual(n2, linked_list.tail)

        n3 = Node(30)
        n4 = Node(44)
        n5 = Node(44)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)

        linked_list.delete(n3.value)
        self.assertEqual(n4, linked_list.head)
        self.assertIsNotNone(linked_list.head.next)
        self.assertEqual(n5, linked_list.head.next)
        self.assertEqual(n5, linked_list.tail)

    def test_delete_last(self):
        n1 = Node(30)
        n2 = Node(44)
        linked_list = LinkedList()
        linked_list.add_in_tail(n1)
        linked_list.add_in_tail(n2)

        linked_list.delete(n2.value)
        self.assertEqual(n1, linked_list.head)
        self.assertEqual(n1, linked_list.tail)

        n3 = Node(30)
        n4 = Node(44)
        n5 = Node(45)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)

        linked_list.delete(n5.value)
        self.assertEqual(n3, linked_list.head)
        self.assertIsNotNone(linked_list.head.next)
        self.assertEqual(n4, linked_list.head.next)
        self.assertEqual(n4, linked_list.tail)

    def test_delete_medium(self):
        n3 = Node(30)
        n4 = Node(44)
        n5 = Node(45)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)

        linked_list.delete(n4.value)
        self.assertEqual(n3, linked_list.head)
        self.assertIsNotNone(linked_list.head.next)
        self.assertEqual(n5, linked_list.head.next)
        self.assertEqual(n5, linked_list.tail)

    def test_delete_with_out_all(self):
        n3 = Node(30)
        n4 = Node(33)
        n5 = Node(44)
        n6 = Node(33)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.add_in_tail(n6)

        linked_list.delete(n4.value)
        self.assertIsNotNone(linked_list.find(33))
        self.assertEqual(n3, linked_list.head)
        self.assertEqual(n5, linked_list.head.next)
        self.assertEqual(n6, linked_list.tail)

    def test_delete_with_all(self):
        n3 = Node(30)
        n4 = Node(33)
        n5 = Node(44)
        n6 = Node(33)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.add_in_tail(n6)

        linked_list.delete(n4.value, True)
        self.assertIsNone(linked_list.find(33))
        self.assertEqual(n3, linked_list.head)
        self.assertEqual(n5, linked_list.head.next)
        self.assertEqual(n5, linked_list.tail)

    def test_clean(self):
        n3 = Node(30)
        n4 = Node(33)
        n5 = Node(44)
        n6 = Node(33)
        linked_list = LinkedList()
        linked_list.add_in_tail(n3)
        linked_list.add_in_tail(n4)
        linked_list.add_in_tail(n5)
        linked_list.add_in_tail(n6)

        linked_list.clean()

        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)


