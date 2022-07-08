import unittest
import sys

from courses.first.bi_directional_list.BiDirectionalListWithDummy import LinkedList2WithDummy, Node, DummyNode

sys.path.append('/var/www/courses')


class LinkedListTest(unittest.TestCase):

    def test_create(self):
        real = Node(2)
        self.assertEqual(2, real.value)
        self.assertIsInstance(real, Node)
        dummy = DummyNode()
        self.assertEqual(None, dummy.value)
        self.assertIsInstance(dummy, DummyNode)

    def test_add_in_tail(self):
        list = LinkedList2WithDummy()
        n1 = Node(20)
        n2 = Node(10)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        # n1 -> n2
        self.assertEqual(n1, list.head.next)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n2, list.tail.prev)

    def test_find(self):
        list = LinkedList2WithDummy()
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
        list = LinkedList2WithDummy()
        list.add_in_tail(Node(5))
        list.add_in_tail(Node(10))
        list.add_in_tail(Node(3))
        list.add_in_tail(Node(4))
        list.add_in_tail(Node(5))

        self.assertEqual(0, len(list.find_all(11)))
        self.assertEqual(1, len(list.find_all(10)))
        self.assertEqual(2, len(list.find_all(5)))

    def test_delete_with_one_el(self):
        list = LinkedList2WithDummy()
        list.delete(5)
        self.assertEqual(list.tail, list.head.next)
        self.assertEqual(list.head, list.tail.prev)

        # n1
        list.add_in_tail(Node(10))
        self.assertIsNotNone(list.find(10))
        list.delete(10)
        self.assertIsNone(list.find(10))
        self.assertIsNone(list.head.next)
        self.assertIsNone(list.tail.prev)

    def test_delete_with_two_els_from_head(self):

        # n1 -> n2
        n1 = Node(10)
        n2 = Node(20)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)

        # n2
        list.delete(10)
        head = list.head.next
        self.assertEqual(n2, head)

    def test_delete_with_two_els_from_tail(self):
        # n1 -> n2
        n1 = Node(10)
        n2 = Node(20)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)

        # n1
        list.delete(20)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1, list.tail.prev)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(list.tail, n1.next)

    def test_delete_with_three_els(self):
        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n2 -> n3
        list.delete(10)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(list.head, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(list.tail, n3.next)
        self.assertEqual(list.tail.prev, n3)

        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n1 -> n3
        list.delete(20)
        self.assertEqual(list.head.next, n1)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n3, n1.next)
        self.assertEqual(n1, n3.prev)
        self.assertEqual(list.tail, n3.next)
        self.assertEqual(list.tail.prev, n3)

        # n1 -> n2 -> n3
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)

        # n1 -> n2
        list.delete(30)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(list.tail, n2.next)
        self.assertEqual(list.tail.prev, n2)

        # n1 -> n2 -> n3 -> n4
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(40)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)

        # n1 -> n2 -> n4
        list.delete(30)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1.prev, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n4, n2.next)
        self.assertEqual(n2, n4.prev)
        self.assertEqual(list.tail, n4.next)
        self.assertEqual(list.tail.prev, n4)

    def test_delete_all(self):
        n1 = Node(10)
        n2 = Node(20)
        n3 = Node(30)
        n4 = Node(20)
        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)

        # n1 -> n3 -> n4
        list.delete(20)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n3, n1.next)
        self.assertEqual(n1, n3.prev)
        self.assertEqual(n4, n3.next)
        self.assertEqual(n3, n4.prev)
        self.assertEqual(n4, list.tail.prev)
        self.assertEqual(n4.next, list.tail)

        list = LinkedList2WithDummy()
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)

        # n1 -> n3
        list.delete(20, True)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1.next, n3)
        self.assertEqual(n1.prev, list.head)
        self.assertEqual(n3.prev, n1)
        self.assertEqual(n3.next, list.tail)
        self.assertEqual(n3, list.tail.prev)

    def test_insert(self):
        list = LinkedList2WithDummy()
        n1 = Node(50)
        n2 = Node(40)
        n3 = Node(30)
        n4 = Node(20)
        n5 = Node(10)
        # n1
        list.insert(None, n1)

        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1, list.tail.prev)

        # n1 -> n2
        list.insert(None, n2)
        self.assertEqual(list.head.next, n1)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n2, list.tail.prev)

        # n1 -> n3 -> n2
        list.insert(n1, n3)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(list.head, n1.prev)
        self.assertEqual(n3, n1.next)
        self.assertEqual(n1, n3.prev)
        self.assertEqual(n2, n3.next)
        self.assertEqual(n3, n2.prev)
        self.assertEqual(list.tail, n2.next)
        self.assertEqual(n2, list.tail.prev)

        # n1 -> n3 -> n2 -> n4
        list.insert(n2, n4)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n3, n1.next)
        self.assertEqual(n1, n3.prev)
        self.assertEqual(n2, n3.next)
        self.assertEqual(n3, n2.prev)
        self.assertEqual(n4, n2.next)
        self.assertEqual(n2, n4.prev)
        self.assertEqual(list.tail, n4.next)
        self.assertEqual(list.tail.prev, n4)

        # n1 -> n3 -> n5 -> n2 -> n4
        list.insert(n3, n5)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1.prev, list.head)
        self.assertEqual(n3, n1.next)
        self.assertEqual(n1, n3.prev)
        self.assertEqual(n5, n3.next)
        self.assertEqual(n3, n5.prev)
        self.assertEqual(n2, n5.next)
        self.assertEqual(n5, n2.prev)
        self.assertEqual(n4, n2.next)
        self.assertEqual(n2, n4.prev)
        self.assertEqual(list.tail, n4.next)
        self.assertEqual(list.tail.prev, n4)

    def test_add_in_head(self):
        n1 = Node(10)
        n2 = Node(20)
        list = LinkedList2WithDummy()
        # n1
        list.add_in_head(n1)
        self.assertEqual(n1, list.head.next)
        self.assertEqual(n1.prev, list.head)
        self.assertEqual(n1.next, list.tail)
        self.assertEqual(n1, list.tail.prev)

        # n2 -> n1
        list.add_in_head(n2)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(n2.prev, list.head)
        self.assertEqual(n1, n2.next)
        self.assertEqual(n1.prev, n2)
        self.assertEqual(n1, list.tail.prev)
        self.assertEqual(n1.next, list.tail)

    def test_clean(self):
        list = LinkedList2WithDummy()
        list.add_in_tail(Node(20))
        list.add_in_tail(Node(30))
        list.add_in_tail(Node(40))
        list.clean()
        self.assertEqual(list.tail, list.head.next)
        self.assertEqual(list.tail.prev, list.head)

    def test_len(self):
        list = LinkedList2WithDummy()
        self.assertEqual(0, list.len())
        list.add_in_tail(Node(20))
        self.assertEqual(1, list.len())
        list.add_in_tail(Node(30))
        self.assertEqual(2, list.len())
        list.add_in_tail(Node(40))
        self.assertEqual(3, list.len())

