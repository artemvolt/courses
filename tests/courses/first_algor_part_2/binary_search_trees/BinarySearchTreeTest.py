import unittest
import sys

from courses.first_algor_part_2.binary_search_trees.BinarySearchTree import BST, BSTFind, BSTNode

sys.path.append('/var/www/courses')


class BinarySearchTreeTest(unittest.TestCase):

    def create_tree(self):
        first = BSTNode(8, 8, None)
        first.LeftChild = fourth = BSTNode(4, 4, first)
        first.RightChild = twelve = BSTNode(12, 12, first)

        fourth.LeftChild = two = BSTNode(2, 2, fourth)
        fourth.RightChild = six = BSTNode(6, 6, fourth)

        twelve.LeftChild = ten = BSTNode(10, 10, twelve)
        twelve.RightChild = fourtheen = BSTNode(14, 14, twelve)

        tree = BST(first)
        return [tree, first, fourth, twelve, two, six, ten, fourtheen]

    def test_find(self):
        tree = BST(None)
        result = tree.FindNodeByKey(0)
        self.assertTrue(result.Node is None)

        # existing key
        testKey = 0
        node = BSTNode(testKey, testKey, None)
        tree = BST(node)
        result = tree.FindNodeByKey(testKey)
        self.assertTrue(result.Node is node)
        self.assertTrue(result.NodeHasKey is True)

        # search existing in right
        [tree, first, fourth, twelve, two, six, ten, fourtheen] = self.create_tree()
        result = tree.FindNodeByKey(14)
        self.assertTrue(result.Node is fourtheen)
        self.assertTrue(result.NodeHasKey is True)

        # search exsiting in left
        result = tree.FindNodeByKey(2)
        self.assertTrue(result.Node is two)
        self.assertTrue(result.NodeHasKey is True)

        # search none exsiting in left
        result = tree.FindNodeByKey(1)
        self.assertEqual(2, result.Node.NodeKey)
        self.assertTrue(result.NodeHasKey is False)
        self.assertTrue(result.ToLeft is True)

        # search none exsiting in right
        result = tree.FindNodeByKey(13)
        self.assertEqual(14, result.Node.NodeKey)
        self.assertTrue(result.NodeHasKey is False)
        self.assertTrue(result.ToLeft is True)

        # search none exsiting in right
        result = tree.FindNodeByKey(15)
        self.assertEqual(14, result.Node.NodeKey)
        self.assertTrue(result.NodeHasKey is False)
        self.assertTrue(result.ToLeft is False)

    def test_add(self):
        tree = BST()
        self.assertFalse(tree.FindNodeByKey(8).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(8, 8)
        )

        root = tree.FindNodeByKey(8).Node
        self.assertTrue(tree.FindNodeByKey(8).NodeHasKey)
        self.assertEqual(root, tree.Root)
        self.assertEqual(8, tree.Root.NodeKey)

        self.assertFalse(tree.FindNodeByKey(12).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(12, 12)
        )
        twelveFound = tree.FindNodeByKey(12)
        twelve = twelveFound.Node
        self.assertTrue(twelveFound.NodeHasKey)
        self.assertEqual(twelve, root.RightChild)
        self.assertIsNone(root.LeftChild)
        self.assertEqual(12, twelve.NodeValue)

        self.assertFalse(tree.FindNodeByKey(4).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(4, 4)
        )
        foundFour = tree.FindNodeByKey(4)
        four = foundFour.Node
        self.assertTrue(tree.FindNodeByKey(4).NodeHasKey)
        self.assertEqual(four, root.LeftChild)
        self.assertEqual(twelve, root.RightChild)

        self.assertFalse(
            tree.AddKeyValue(4, 4)
        )
        self.assertFalse(
            tree.AddKeyValue(12, 12)
        )
        self.assertEqual(tree.Root, root)
        self.assertEqual(twelve, root.RightChild)
        self.assertEqual(four, root.LeftChild)

        self.assertFalse(tree.FindNodeByKey(2).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(2, 2)
        )
        foundTwo = tree.FindNodeByKey(2)
        two = foundTwo.Node
        self.assertTrue(foundTwo.NodeHasKey)
        self.assertEqual(two, four.LeftChild)
        self.assertFalse(
            tree.AddKeyValue(2, 2)
        )

        self.assertFalse(tree.FindNodeByKey(6).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(6, 6)
        )
        foundSix = tree.FindNodeByKey(6)
        six = foundSix.Node
        self.assertTrue(foundSix.NodeHasKey)
        self.assertEqual(six, four.RightChild)
        self.assertFalse(
            tree.AddKeyValue(6, 6)
        )

        self.assertFalse(tree.FindNodeByKey(10).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(10, 10)
        )
        foundTen = tree.FindNodeByKey(10)
        ten = foundTen.Node
        self.assertTrue(foundTen.NodeHasKey)
        self.assertEqual(ten, twelve.LeftChild)

        self.assertFalse(tree.FindNodeByKey(9).NodeHasKey)
        self.assertTrue(
            tree.AddKeyValue(9, 9)
        )
        foundNine = tree.FindNodeByKey(9)
        nine = foundNine.Node
        self.assertTrue(foundNine.NodeHasKey)
        self.assertEqual(nine, ten.LeftChild)

    def test_find_max(self):
        [tree, first, fourth, twelve, two, six, ten, fourtheen] = self.create_tree()
        self.assertEqual(fourtheen, tree.FinMinMax(tree.Root, True))
        self.assertEqual(two, tree.FinMinMax(tree.Root, False))

        self.assertEqual(fourtheen, tree.FinMinMax(twelve, True))
        self.assertEqual(ten, tree.FinMinMax(twelve, False))

        self.assertEqual(six, tree.FinMinMax(fourth, True))
        self.assertEqual(two, tree.FinMinMax(fourth, False))

        self.assertEqual(ten, tree.FinMinMax(ten, True))
        self.assertEqual(ten, tree.FinMinMax(ten, False))

    def test_count(self):
        tree = BST()
        self.assertEqual(0, tree.Count())
        [tree, first, fourth, twelve, two, six, ten, fourtheen] = self.create_tree()
        self.assertEqual(7, tree.Count())

    def test_delete(self):
        tree = BST(None)
        self.assertFalse(tree.DeleteNodeByKey(0))

        [tree, first, fourth, twelve, two, six, ten, fourtheen] = self.create_tree()
        self.assertTrue(tree.FindNodeByKey(10).NodeHasKey)
        tree.DeleteNodeByKey(10)
        self.assertFalse(tree.FindNodeByKey(10).NodeHasKey)
        self.assertEqual(first, tree.Root)
        self.assertEqual(fourth, first.LeftChild)
        self.assertEqual(twelve, first.RightChild)
        self.assertEqual(None, twelve.LeftChild)
        self.assertEqual(fourtheen, twelve.RightChild)

        self.assertTrue(tree.FindNodeByKey(4).NodeHasKey)
        tree.DeleteNodeByKey(4)
        self.assertFalse(tree.FindNodeByKey(4).NodeHasKey)
        self.assertEqual(first, tree.Root)
        self.assertEqual(six, first.LeftChild)
        self.assertEqual(twelve, first.RightChild)

    def test_delete_root(self):
        tree = BST(BSTNode(1, 1, None))
        self.assertTrue(tree.FindNodeByKey(1).NodeHasKey)
        self.assertTrue(tree.DeleteNodeByKey(1))
        self.assertFalse(tree.FindNodeByKey(1).NodeHasKey)
        self.assertTrue(tree.Root is None)

