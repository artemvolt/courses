import unittest
import sys

from courses.first_algor_part_2.first_tree.SimpleTree import SimpleTree, SimpleTreeNode

sys.path.append('/var/www/courses')


class SimpleTreeTest(unittest.TestCase):

    def test_add_child(self):
        tree = SimpleTree(None)
        self.assertIsNone(tree.Root)
        root_node = SimpleTreeNode(1, None)
        tree.AddChild(None, root_node)
        self.assertIsNotNone(tree.Root)
        self.assertFalse(tree.Root.HasChildren())
        parent_two_node = SimpleTreeNode(2, None)
        tree.AddChild(root_node, parent_two_node)
        self.assertTrue(root_node.HasChildren())
        self.assertEqual(root_node, parent_two_node.Parent)
        self.assertEqual(root_node.Children[0], parent_two_node)

    def test_count(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.Count())
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        tree.AddChild(main_node, root_node_one)
        self.assertEqual(1, tree.Count())
        tree.AddChild(main_node, root_node_two)
        self.assertEqual(1, tree.Count())
        tree.AddChild(root_node_one, parent_root_node_one)
        self.assertEqual(2, tree.Count())
        tree.AddChild(root_node_two, parent_root_node_two)
        self.assertEqual(3, tree.Count())
        root_node_three = SimpleTreeNode(5, None)
        tree.AddChild(main_node, root_node_three)
        self.assertEqual(3, tree.LeafCount())

    def test_leaf_count(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.LeafCount())
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        self.assertEqual(1, tree.LeafCount())
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        tree.AddChild(main_node, root_node_one)
        self.assertEqual(1, tree.LeafCount())
        tree.AddChild(main_node, root_node_two)
        self.assertEqual(2, tree.LeafCount())
        tree.AddChild(root_node_one, parent_root_node_one)
        self.assertEqual(2, tree.LeafCount())
        tree.AddChild(root_node_two, parent_root_node_two)
        self.assertEqual(2, tree.LeafCount())
        root_node_three = SimpleTreeNode(5, None)
        tree.AddChild(main_node, root_node_three)
        self.assertEqual(3, tree.LeafCount())

    def test_delete_node(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        root_node_two = SimpleTreeNode(2, None)
        root_node_three = SimpleTreeNode(5, None)

        parent_root_node_one = SimpleTreeNode(3, None)
        parent_root_node_two = SimpleTreeNode(4, None)

        # 999 -> [1 -> [3],2 -> [4], 5]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)

        # 999 -> [1 -> [3], 5]
        tree.DeleteNode(root_node_two)
        self.assertEqual(2, len(main_node.Children))
        self.assertEqual(5, main_node.Children[0].NodeValue)
        self.assertEqual(1, main_node.Children[1].NodeValue)

        # 999 -> [5]
        tree.DeleteNode(root_node_one)
        self.assertEqual(1, len(main_node.Children))
        self.assertEqual(5, main_node.Children[0].NodeValue)

    def test_get_all_nodes(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        root_node_two = SimpleTreeNode(2, None)
        root_node_three = SimpleTreeNode(5, None)

        parent_root_node_one = SimpleTreeNode(3, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        parent_root_node_two_one = SimpleTreeNode(7, None)
        parent_root_node_two_two = SimpleTreeNode(8, None)

        # 999 -> [
        #   1 -> [3],
        #   2 -> [
        #       4 => [7, 8]
        #   ],
        #   5
        #   ]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)
        tree.AddChild(parent_root_node_two, parent_root_node_two_one)
        tree.AddChild(parent_root_node_two, parent_root_node_two_two)

        nodes = tree.GetAllNodes()
        self.assertEqual(4, len(nodes))
        self.assertEqual(999, nodes[0].NodeValue)
        self.assertEqual(1, nodes[1].NodeValue)
        self.assertEqual(2, nodes[2].NodeValue)
        self.assertEqual(4, nodes[3].NodeValue)

    def test_find_nodes_by_value(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        root_node_two = SimpleTreeNode(2, None)
        root_node_three = SimpleTreeNode(5, None)

        parent_root_node_one = SimpleTreeNode(3, None)
        parent_root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two_one = SimpleTreeNode(7, None)
        parent_root_node_two_two = SimpleTreeNode(2, None)

        # 999 -> [
        #   1 -> [3],
        #   2 -> [
        #       2 => [7, 2]
        #   ],
        #   5
        #   ]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)
        tree.AddChild(parent_root_node_two, parent_root_node_two_one)
        tree.AddChild(parent_root_node_two, parent_root_node_two_two)

        nodes = tree.FindNodesByValue(2)
        self.assertEqual(2, len(nodes))
        self.assertEqual(2, nodes[0].NodeValue)
        children_first = nodes[0].Children
        self.assertEqual(1, len(children_first))
        self.assertEqual(2, children_first[0].NodeValue)

        children_second = nodes[1].Children
        self.assertEqual(2, len(children_second))
        self.assertEqual(7, children_second[0].NodeValue)
        self.assertEqual(2, children_second[1].NodeValue)

    def test_move_node(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        root_node_two = SimpleTreeNode(2, None)
        root_node_three = SimpleTreeNode(5, None)

        parent_root_node_one = SimpleTreeNode(3, None)
        parent_root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two_one = SimpleTreeNode(7, None)
        parent_root_node_two_two = SimpleTreeNode(2, None)

        # 999 -> [
        #   1 -> [3],
        #   2 -> [
        #       2 => [7, 2]
        #   ],
        #   5
        #   ]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)
        tree.AddChild(parent_root_node_two, parent_root_node_two_one)
        tree.AddChild(parent_root_node_two, parent_root_node_two_two)


        # 999 -> [
        #   1 -> [
        #       3 => [
        #           2 => [7, 2]
        #       ]
        #   ],
        #   2 -> [],
        #   5
        # ]
        tree.MoveNode(parent_root_node_two, parent_root_node_one)
        moved = tree.Root.Children[1]  # 1
        next = moved.Children[0]
        self.assertEqual(1, moved.NodeValue)
        self.assertEqual(3, next.NodeValue)
        self.assertEqual(1, len(next.Children))
        self.assertEqual(2, next.Children[0].NodeValue)
        next = next.Children[0]
        self.assertEqual(2, len(next.Children))
        self.assertEqual(7, next.Children[0].NodeValue)
        self.assertFalse(next.Children[0].HasChildren())
        self.assertFalse(next.Children[1].HasChildren())

        five = tree.Root.Children[0]  # 5
        self.assertEqual(5, five.NodeValue)
        self.assertEqual(0, len(five.Children))

        two = tree.Root.Children[2] # 2
        #print(two.Children[0].Children[1].NodeValue)
        self.assertEqual(2, two.NodeValue)
        self.assertEqual(0, len(two.Children))
        # self.assertEqual(7, next.Children[0].NodeValue)
        # self.assertEqual(2, next.Children[1].NodeValue)
        # print(two.NodeValue)

        # tree.MoveNode(parent_root_node_two_one, root_node_three)
