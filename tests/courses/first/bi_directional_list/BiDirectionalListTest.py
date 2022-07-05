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

    def test_delete_with_one_el(self):
        list = LinkedList2()
        list.delete(5)

        # n1
        list.add_in_tail(Node(10))
        self.assertIsNotNone(list.find(10))
        list.delete(10)
        self.assertIsNone(list.find(10))
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)

    def test_delete_with_two_els(self):

        # n1 -> n2
        n1 = Node(10)
        n2 = Node(20)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)

        # n2
        list.delete(10)
        self.assertEqual(n2, list.head)
        self.assertEqual(n2, list.tail)

    def test_delete_with_two_els_from_tail(self):
        # n1 -> n2
        n1 = Node(10)
        n2 = Node(20)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)

        # n1
        list.delete(20)
        self.assertEqual(n1, list.head)
        self.assertEqual(n1, list.tail)

    def test_delete_with_three_els(self):
        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n2 -> n3
        list.delete(10)
        self.assertEqual(n2, list.head)
        self.assertEqual(n3, list.head.next)
        self.assertEqual(n3, list.tail)

        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n1 -> n3
        list.delete(20)
        self.assertEqual(n1, list.head)
        self.assertEqual(n3, list.head.next)
        self.assertEqual(n3, list.tail)

        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n1 -> n2
        list.delete(30)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(n2, list.tail)

        # n1 -> n2 -> n3 -> n4
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        list = LinkedList2()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)

        # n1 -> n2 -> n4
        list.delete(30)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(n4, list.head.next.next)
        self.assertEqual(n4, list.tail)




