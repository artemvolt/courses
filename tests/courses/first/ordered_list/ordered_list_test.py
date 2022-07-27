import sys
import unittest
# noinspection PyUnresolvedReferences
from unittest_data_provider import data_provider

from courses.first.ordered_list.ordered_list import OrderedList, OrderedStringList

sys.path.append('/var/www/courses')


# noinspection DuplicatedCode
class ordered_list_test(unittest.TestCase):
    def test_compare(self):
        list = OrderedList(True)
        self.assertEqual(-1, list.compare(1, 2))
        self.assertEqual(1, list.compare(2, 1))
        self.assertEqual(0, list.compare(1, 1))

    def test_add_asc(self):
        list = OrderedList(True)
        list.add(2)
        self.assertEqual(2, list.head.value)
        self.assertEqual(2, list.tail.value)
        list.add(4)
        self.assertEqual(2, list.head.value)
        self.assertEqual(4, list.head.next.value)
        self.assertEqual(4, list.tail.value)
        self.assertEqual(2, list.tail.prev.value)
        list.add(3)
        # 2 - 3 - 4
        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        self.assertEqual(2, n1.value)
        self.assertEqual(3, n2.value)
        self.assertEqual(4, n3.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(2, n1.value)
        self.assertEqual(n2, n1.next)
        self.assertEqual(None, n1.prev)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(list.tail, n3)
        # 2 - 3 - 4 - 5
        list.add(5)
        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        n4 = n3.next
        self.assertEqual(2, n1.value)
        self.assertEqual(3, n2.value)
        self.assertEqual(4, n3.value)
        self.assertEqual(5, n4.value)
        self.assertEqual(list.head, n1)
        self.assertEqual(None, n1.prev)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(n4, n3.next)
        self.assertEqual(n3, n4.prev)
        self.assertEqual(None, n4.next)
        self.assertEqual(list.tail, n4)

    def test_add_desc(self):
        list = OrderedList(False)
        list.add(2)
        self.assertEqual(2, list.head.value)
        self.assertEqual(2, list.tail.value)
        list.add(4)
        n1 = list.head
        n2 = n1.next
        self.assertEqual(4, n1.value)
        self.assertEqual(2, n2.value)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, list.tail)

        list.add(3)
        # 4 - 3 - 2
        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        self.assertEqual(4, n1.value)
        self.assertEqual(3, n2.value)
        self.assertEqual(2, n3.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(None, n1.prev)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(list.tail, n3)
        # 5 - 4 - 3 - 2
        list.add(5)
        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        n4 = n3.next
        self.assertEqual(5, n1.value)
        self.assertEqual(4, n2.value)
        self.assertEqual(3, n3.value)
        self.assertEqual(2, n4.value)
        self.assertEqual(list.head, n1)
        self.assertEqual(None, n1.prev)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(n4, n3.next)
        self.assertEqual(n3, n4.prev)
        self.assertEqual(None, n4.next)
        self.assertEqual(list.tail, n4)

    def test_strings(self):
        list = OrderedStringList(True)
        list.add('abc')
        self.assertEqual('abc', list.head.value)
        list.add('bca')
        list.add('gfg')
        n1 = list.head
        n2 = list.head.next
        n3 = n2.next
        self.assertEqual('abc', n1.value)
        self.assertEqual('bca', n2.value)
        self.assertEqual('gfg', n3.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(n3, list.tail)

    def test_strings_desc(self):
        list = OrderedStringList(False)
        list.add('abc')
        self.assertEqual('abc', list.head.value)
        list.add('bca')
        list.add('gfg')
        n1 = list.head
        n2 = list.head.next
        n3 = n2.next
        self.assertEqual('gfg', n1.value)
        self.assertEqual('bca', n2.value)
        self.assertEqual('abc', n3.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, list.head.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(n3, list.tail)

    def test_string_compare(self):
        list = OrderedStringList(True)
        self.assertEqual(-1, list.compare('abc', 'bca'))
        self.assertEqual(0, list.compare('abc', 'abc'))
        self.assertEqual(1, list.compare('bca', 'abc'))

    def test_find(self):
        list = OrderedList(True)
        self.assertEqual(None, list.find(1))
        list.add(1)
        list.add(3)
        list.add(4)
        # 1 - 3 - 4
        self.assertEqual(1, list.find(1).value)
        self.assertEqual(3, list.find(3).value)
        self.assertIsNone(list.find(2))

        list = OrderedList(False)
        self.assertEqual(None, list.find(1))
        list.add(1)
        list.add(3)
        list.add(4)
        # 4 - 3 - 1
        self.assertEqual(1, list.find(1).value)
        self.assertIsNone(list.find(2))
        self.assertEqual(3, list.find(3).value)
        self.assertEqual(4, list.find(4).value)
        self.assertEqual(None, list.find(5))

    def test_size(self):
        list = OrderedList(True)
        self.assertEqual(0, list.len())
        list.add(1)
        self.assertEqual(1, list.len())
        list.add(2)
        self.assertEqual(2, list.len())

    def test_delete_from_head(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.delete(1)

        n1 = list.head
        n2 = n1.next
        self.assertEqual(2, n1.value)
        self.assertEqual(3, n2.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n2, list.tail)
        self.assertIsNone(n2.next)
        self.assertIsNone(n1.prev)

    def test_delete_from_tail(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.delete(3)

        n1 = list.head
        n2 = n1.next
        self.assertEqual(1, n1.value)
        self.assertEqual(2, n2.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n2, list.tail)
        self.assertIsNone(n2.next)
        self.assertIsNone(n1.prev)

    def test_delete_from_middle(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.delete(2)

        n1 = list.head
        n2 = n1.next
        self.assertEqual(1, n1.value)
        self.assertEqual(3, n2.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n2, list.tail)
        self.assertIsNone(n2.next)
        self.assertIsNone(n1.prev)

    def test_delete_step(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)

        self.assertEqual(1, list.head.value)
        list.delete(1)
        self.assertEqual(2, list.head.value)
        list.delete(2)
        self.assertEqual(3, list.head.value)
        list.delete(3)
        self.assertEqual(4, list.head.value)
        list.delete(4)
        self.assertIsNone(list.head)

    def test_delete_none_existing(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.delete(4)

        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        self.assertEqual(1, n1.value)
        self.assertEqual(2, n2.value)
        self.assertEqual(3, n3.value)
        self.assertEqual(n1, list.head)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertEqual(n3, list.tail)
        self.assertIsNone(n3.next)
        self.assertIsNone(n1.prev)

    def test_delete_in_empty(self):
        list = OrderedList(True)
        list.delete(4)

        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)

    def test_delete_double(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(2)
        list.add(4)

        list.delete(2)
        n1 = list.head
        n2 = n1.next
        n3 = n2.next
        self.assertEqual(1, n1.value)
        self.assertEqual(2, n2.value)
        self.assertEqual(4, n3.value)
        self.assertEqual(n2, n1.next)
        self.assertEqual(n1, n2.prev)
        self.assertEqual(n3, n2.next)
        self.assertEqual(n2, n3.prev)
        self.assertIsNone(n3.next)

    def test_delete_sort(self):
        list = OrderedList(False)
        list.add(1)
        list.delete(1)
        self.assertEqual(0, list.len())
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        list.add(1)
        list.add(2)
        list.delete(1)
        self.assertEqual(2, list.head.value)
        self.assertEqual(2, list.tail.value)
        list.add(1)
        list.delete(2)
        self.assertEqual(1, list.head.value)
        self.assertEqual(1, list.tail.value)
        list.add(2)
        list.add(3)

        # 3 - 1
        list.delete(2)
        n1 = list.head
        n2 = n1.next
        self.assertEqual(3, n1.value)
        self.assertEqual(1, n2.value)

    def test_clean_asc(self):
        list = OrderedList(True)
        list.add(1)
        list.add(2)
        list.add(3)
        list.clean(True)
        self.assertIsNone(list.head)
        self.assertIsNone(list.tail)
        self.assertEqual(0, list.len())

    itemIds = lambda: (
        ([], 1, []),
        ([1], 1, []),
        ([2], 1, [2]),
        ([1, 2, 3], 1, [2, 3]),
        ([1, 2, 3], 3, [1, 2]),
        ([1, 2, 3], 2, [1, 3]),
    )

    @data_provider(itemIds)
    def test_delete__ascending(self, income_list, item_for_delete, expected_list):
        o_list_1 = OrderedList(True)
        for i in income_list:
            o_list_1.add(i)

        o_list_1.delete(item_for_delete)
        result_simple = []
        for x in o_list_1.get_all():
            result_simple.append(x.value)

        self.assertEqual(result_simple, expected_list)

    @data_provider(itemIds)
    def test_delete_desc(self, income_list, item_for_delete, expected_list):
        o_list_1 = OrderedList(False)
        for i in reversed(income_list):
            o_list_1.add(i)

        o_list_1.delete(item_for_delete)
        result_simple = []
        for x in o_list_1.get_all():
            result_simple.append(x.value)

        self.assertEqual(result_simple, list(reversed(expected_list)))
