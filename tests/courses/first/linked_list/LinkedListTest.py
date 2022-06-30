import unittest
import sys

sys.path.append('/var/www/courses')

# noinspection PyPep8
from courses.first.linked_list.LinkedList import Node, LinkedList


class LinkedListTest(unittest.TestCase):
    def test_delete_empty(self):
        linked_list = LinkedList()

        linked_list.delete(30)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

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

    def test_find_all(self):
        n3 = Node(30)
        n4 = Node(30)
        n5 = Node(30)

        linked_list = LinkedList()
        found = linked_list.find_all(n3.value)
        self.assertEqual(0, len(found))

        linked_list.add_in_tail(n3)
        found = linked_list.find_all(n3.value)
        self.assertEqual(1, len(found))

        linked_list.add_in_tail(n4)
        found = linked_list.find_all(n3.value)
        self.assertEqual(2, len(found))

        linked_list.add_in_tail(n5)
        found = linked_list.find_all(n3.value)
        self.assertEqual(3, len(found))

    def test_len(self):
        n3 = Node(30)
        n4 = Node(30)

        linked_list = LinkedList()
        self.assertEqual(0, linked_list.len())

        linked_list.add_in_tail(n3)
        self.assertEqual(1, linked_list.len())

        linked_list.add_in_tail(n4)
        self.assertEqual(2, linked_list.len())

    def test_insert(self):
        n3 = Node(31)
        n4 = Node(32)
        n5 = Node(33)
        n6 = Node(33)
        n7 = Node(33)

        linked_list = LinkedList()
        linked_list.insert(None, n3)
        self.assertEqual(1, linked_list.len())
        self.assertEqual(n3, linked_list.head)
        self.assertEqual(n3, linked_list.tail)

        linked_list.insert(None, n4)
        self.assertEqual(2, linked_list.len())
        self.assertEqual(n4, linked_list.head)
        self.assertEqual(n3, linked_list.head.next)
        self.assertEqual(n3, linked_list.tail)

        # добавляем в середину
        # на выходе: n4 -> n5 -> n3
        linked_list.insert(n4, n5)
        self.assertEqual(n4, linked_list.head)
        self.assertEqual(n5, linked_list.head.next)
        self.assertEqual(n3, linked_list.head.next.next)
        self.assertEqual(n3, linked_list.tail)

        # добавляем в конец
        # на выходе: n4 -> n5 -> n3 -> n6
        linked_list.insert(n3, n6)
        self.assertEqual(n4, linked_list.head)
        self.assertEqual(n5, n4.next)
        self.assertEqual(n3, n5.next)
        self.assertEqual(n6, n3.next)
        self.assertEqual(n6, linked_list.tail)

        # и еще раз в середину
        # на выходе: n4 -> n5 -> n7 -> n3 -> n6
        linked_list.insert(n5, n7)
        self.assertEqual(n4, linked_list.head)
        self.assertEqual(n5, n4.next)
        self.assertEqual(n7, n5.next)
        self.assertEqual(n3, n7.next)
        self.assertEqual(n6, n3.next)
        self.assertEqual(n6, linked_list.tail)
