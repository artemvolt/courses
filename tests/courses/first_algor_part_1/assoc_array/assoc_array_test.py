import unittest
import sys

from courses.first_algor_part_1.assoc_array.NativeDictionary import NativeDictionary

sys.path.append('/var/www/courses')


class AssocArrayTest(unittest.TestCase):

    def test_hash(self):
        assoc = NativeDictionary(17)
        self.assertIsNotNone(assoc.hash_fun(''))
        self.assertIsNotNone(assoc.hash_fun('abc'))
        self.assertEqual(assoc.hash_fun('abc'), assoc.hash_fun('abc'))

    def test_put(self):
        assoc = NativeDictionary(17)
        assoc.put('name', 'John')
        self.assertTrue('name' in assoc.slots)
        self.assertTrue('John' in assoc.values)
        index = assoc.slots.index('name')
        self.assertEqual('John', assoc.values[index])
        assoc.put('name', 'John #1')
        self.assertTrue('name' in assoc.slots)
        self.assertFalse('John' in assoc.values)
        self.assertTrue('John #1' in assoc.values)

    def test_collizion(self):
        assoc = NativeDictionary(17)
        assoc.put('abc', 'John #1')
        assoc.put('cba', 'John #2')
        self.assertTrue('abc' in assoc.slots)
        self.assertTrue('cba' in assoc.slots)
        self.assertTrue('John #1' in assoc.values)
        self.assertTrue('John #2' in assoc.values)
        self.assertEqual('John #1', assoc.get('abc'))
        self.assertEqual('John #2', assoc.get('cba'))
        assoc.put('cba', 'John #3')
        self.assertTrue('John #1' in assoc.values)
        self.assertFalse('John #2' in assoc.values)
        self.assertTrue('John #3' in assoc.values)
        self.assertTrue('John #3', assoc.get("cba"))
        self.assertTrue('John #1', assoc.get("abc"))

    def test_is_key(self):
        assoc = NativeDictionary(17)
        self.assertFalse(assoc.is_key('name'))
        assoc.put('name', 'John')
        self.assertTrue(assoc.is_key('name'))

    def test_get(self):
        assoc = NativeDictionary(17)
        assoc.put('name', 'John')
        self.assertIsNone(assoc.get('name1'))
        self.assertEqual('John', assoc.get('name'))
