import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first_algor_part_2.six_balanced_tree.BalancedTree import BSTNode, BalancedBST


class BalancedBSTTests(unittest.TestCase):
    def test_generate_empty(self):
        result = BalancedBST().GenerateTree([])
        self.assertTrue(result.Root is None)

    def test_GenerateTreeWithOneNode(self):
        result = BalancedBST().GenerateTree([0])
        self.assertTrue(isinstance(result.Root, BSTNode))
        self.assertTrue(result.Root.NodeKey == 0)
        self.assertTrue(result.Root.Parent is None)
        self.assertTrue(result.Root.LeftChild is None)
        self.assertTrue(result.Root.RightChild is None)
        self.assertTrue(result.Root.Level == 0)

    def test_GenerateTreeWithTwoNodes(self):
        result = BalancedBST().GenerateTree([0, 1])
        self.assertTrue(isinstance(result.Root, BSTNode))
        self.assertTrue(result.Root.NodeKey == 1)
        self.assertTrue(result.Root.Parent is None)
        self.assertTrue(isinstance(result.Root.LeftChild, BSTNode))
        self.assertTrue(result.Root.RightChild is None)
        self.assertTrue(result.Root.Level == 0)

    def test_IsBalancedEmpty(self):
        tree = BalancedBST()
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_IsBalancedOneNode(self):
        tree = BalancedBST()
        tree.GenerateTree([0])
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_IsBalancedTwoNodes(self):
        tree = BalancedBST()
        tree.GenerateTree([0, 1])
        self.assertTrue(tree.IsBalanced(tree.Root))
