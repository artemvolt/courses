import sys
import unittest

from courses.first.power_set.PowerSet import PowerSet

sys.path.append('/var/www/courses')


# noinspection DuplicatedCode
class PowerSetTest(unittest.TestCase):
    def test_size(self):
        set = PowerSet()
        self.assertEqual(0, set.size())
        set.put(1)
        self.assertEqual(1, set.size())
        set.put(2)
        self.assertEqual(2, set.size())
        set.remove(2)
        self.assertEqual(1, set.size())
        set.remove(1)
        self.assertEqual(0, set.size())

    def test_put(self):
        set = PowerSet()
        set.put(1)
        self.assertTrue(1 in set.values)
        set.put(2)
        self.assertTrue(2 in set.values)
        set.put(2)
        self.assertTrue(2 in set.values)
        self.assertEqual(2, set.size())

    def test_get(self):
        set = PowerSet()
        self.assertFalse(set.get(1))
        set.put(1)
        self.assertTrue(set.get(1))
        set.put(2)
        self.assertTrue(set.get(2))

    def test_remove(self):
        set = PowerSet()
        self.assertFalse(set.remove(1))
        set.put(1)
        self.assertTrue(set.remove(1))
        set.put(2)
        self.assertTrue(set.remove(2))
        self.assertFalse(set.remove(2))

    def test_intersection_none(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(4)
        set2.put(5)
        set2.put(6)
        set3 = set1.intersection(set2)
        self.assertEqual(0, set3.size())

    def test_intersection_one(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set1.put(4)
        set2 = PowerSet()
        set2.put(4)
        set2.put(5)
        set2.put(6)
        set3 = set1.intersection(set2)
        self.assertEqual(1, set3.size())
        self.assertTrue(set3.get(4))

    def test_intersection_one_revert(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(3)
        set2.put(4)
        set2.put(5)
        set2.put(6)
        set3 = set1.intersection(set2)
        self.assertEqual(1, set3.size())
        self.assertTrue(set3.get(3))

    def test_intersection_union(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(3)
        set2.put(4)
        set2.put(5)
        set2.put(6)
        set3 = set1.union(set2)
        self.assertEqual(6, set3.size())
        self.assertTrue(set3.get(1))
        self.assertTrue(set3.get(2))
        self.assertTrue(set3.get(3))
        self.assertTrue(set3.get(4))
        self.assertTrue(set3.get(5))
        self.assertTrue(set3.get(6))

    def test_intersection_difference(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(3)
        set2.put(4)
        set2.put(5)
        set2.put(6)
        set3 = set1.difference(set2)
        self.assertEqual(2, set3.size())
        self.assertTrue(set3.get(1))
        self.assertTrue(set3.get(2))

    def test_intersection_difference_same(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(1)
        set2.put(2)
        set2.put(3)
        set3 = set1.difference(set2)
        self.assertEqual(0, set3.size())

    def test_intersection_difference_same_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        set3 = set1.difference(set2)
        self.assertEqual(0, set3.size())

    def test_intersection_issubset_same(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(1)
        set2.put(2)
        set2.put(3)
        self.assertTrue(set1.issubset(set2))

    def test_intersection_issubset_bigger_with_revert(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set1.put(4)
        set2 = PowerSet()
        set2.put(1)
        set2.put(2)
        set2.put(3)
        self.assertTrue(set1.issubset(set2))
        self.assertFalse(set2.issubset(set1))

    def test_intersection_issubset_bigger(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        set2 = PowerSet()
        set2.put(1)
        set2.put(2)
        set2.put(3)
        set2.put(4)
        self.assertTrue(set2.issubset(set1))
