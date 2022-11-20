import unittest
import sys

from courses.first_algor_part_2.four_binary_trees.BinaryTree import aBST

sys.path.append('/var/www/courses')


class BinaryTreeTest(unittest.TestCase):

    def create_tree(self):
        tree = aBST(3)
        tree.Tree = [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92]
        return tree

    def test_size(self):
        tree = aBST(0)
        self.assertEqual(1, len(tree.Tree))
        tree = aBST(1)
        self.assertEqual(3, len(tree.Tree))
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        tree = aBST(3)
        self.assertEqual(15, len(tree.Tree))

    def test_add_key(self):
        tree = aBST(0)
        self.assertEqual(0, tree.AddKey(1))
        self.assertEqual(-1, tree.AddKey(2))
        self.assertEqual(0, tree.AddKey(1))

        tree = self.create_tree()
        self.assertEqual(1, tree.AddKey(25))
        self.assertEqual(4, tree.AddKey(37))
        self.assertEqual(5, tree.AddKey(62))
        self.assertEqual(3, tree.AddKey(20))
        self.assertEqual(3, tree.AddKey(20))
        self.assertEqual(7, tree.AddKey(15))
        self.assertEqual(8, tree.AddKey(23))
        self.assertEqual(13, tree.AddKey(80))

    def test_find_key_index(self):
        tree = aBST(0)
        self.assertEqual(0, tree.FindKeyIndex(1))
        self.assertEqual(0, tree.FindKeyIndex(2))
        self.assertEqual(0, tree.AddKey(1))
        self.assertEqual(0, tree.FindKeyIndex(1))
        self.assertEqual(None, tree.FindKeyIndex(2))

        tree = self.create_tree()
        self.assertEqual(1, tree.FindKeyIndex(25))
        self.assertEqual(4, tree.FindKeyIndex(37))
        self.assertEqual(5, tree.FindKeyIndex(62))
        self.assertEqual(-3, tree.FindKeyIndex(20))
        self.assertEqual(-3, tree.FindKeyIndex(15))
        self.assertEqual(-3, tree.FindKeyIndex(23))
        self.assertEqual(-13, tree.FindKeyIndex(80))


