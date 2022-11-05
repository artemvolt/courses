import unittest
import sys

from courses.first.hash.hash_table import HashTable

sys.path.append('/var/www/courses')


class HashTableTest(unittest.TestCase):

    def test_hash(self):
        table = HashTable(17, 1)
        self.assertIsNotNone(table.hash_fun(''))
        self.assertIsNotNone(table.hash_fun('abc'))
        self.assertEqual(table.hash_fun('abc'), table.hash_fun('abc'))

    def test_seek_slot(self):
        table = HashTable(3, 1)
        self.assertIsNotNone(table.seek_slot('abc'))
        self.assertEqual(0, table.seek_slot('abc'))
        table.slots[0] = 'abc'
        self.assertIsNotNone(table.seek_slot('abc'))
        self.assertEqual(1, table.seek_slot('abc'))
        table.slots[1] = 'abc'
        self.assertIsNotNone(table.seek_slot('abc'))
        self.assertEqual(2, table.seek_slot('abc'))
        table.slots[2] = 'abc'
        self.assertIsNone(table.seek_slot('abc'))

    def test_put(self):
        table = HashTable(3, 1)
        self.assertEqual(0, table.put('abc'))
        self.assertEqual(1, table.put('abc'))
        self.assertEqual(2, table.put('abc'))
        self.assertIsNone(table.put('abc'))

    def test_put_other_strings_with_same_hash(self):
        table = HashTable(3, 1)
        self.assertEqual(0, table.put('abc'))
        self.assertEqual(1, table.put('cba'))
        self.assertEqual(2, table.put('bac'))
        self.assertIsNone(table.put('abc'))

    def test_find(self):
        table = HashTable(3, 1)
        self.assertIsNone(table.find('abc'))
        table.put('abc')
        self.assertEqual(0, table.find('abc'))
        table.put('bca')
        self.assertEqual(0, table.find('abc'))
        self.assertEqual(1, table.find('bca'))
