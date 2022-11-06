import unittest
import sys

from courses.first_algor_part_2.first_tree.SimpleTree import SimpleTree, SimpleTreeNode

sys.path.append('/var/www/courses')


class SimpleTreeTest(unittest.TestCase):

    def test_add_child(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        parent_root_node_two_child = SimpleTreeNode(10, None)
        # 999 => [1]
        tree.AddChild(main_node, root_node_one)
        # 999 => [1, 2]
        tree.AddChild(main_node, root_node_two)
        # 999 => [
        #   1 => [3],
        #   2
        # ]
        #
        tree.AddChild(root_node_one, parent_root_node_one)
        # 999 => [
        #   1 => [3],
        #   2 => [4]
        # ]
        tree.AddChild(root_node_two, parent_root_node_two)
        root_node_three = SimpleTreeNode(5, None)
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(parent_root_node_two, parent_root_node_two_child)
        # 999 => [
        #   1 => [3],
        #   2 => [4 => [10]],
        #   5
        # ]
        main = tree.Root
        self.assertEqual(999, main.NodeValue)
        self.assertTrue(main.HasChildren())
        children = main.Children
        self.assertEqual(3, len(children))
        [first, second, third] = children
        self.assertEqual(1, first.NodeValue)
        self.assertEqual(2, second.NodeValue)
        self.assertEqual(5, third.NodeValue)
        self.assertEqual(1, len(first.Children))
        self.assertEqual(1, len(second.Children))
        self.assertEqual(0, len(third.Children))
        self.assertEqual(3, first.Children[0].NodeValue)
        self.assertFalse(first.Children[0].HasChildren())
        forth = second.Children[0]
        self.assertEqual(4, forth.NodeValue)
        self.assertTrue(forth.HasChildren())
        self.assertEqual(10, forth.Children[0].NodeValue)
        self.assertFalse(forth.Children[0].HasChildren())

    def test_count_and_leaf_count(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.Count())
        main_node = SimpleTreeNode(999, None)
        # [ 999 ]
        tree.AddChild(None, main_node)
        self.assertEqual(0, tree.Count())
        self.assertEqual(1, tree.LeafCount())
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        parent_root_node_two_child = SimpleTreeNode(10, None)
        # 999 => [1]
        tree.AddChild(main_node, root_node_one)
        self.assertEqual(1, tree.Count())
        self.assertEqual(1, tree.LeafCount())
        # 999 => [1, 2]
        tree.AddChild(main_node, root_node_two)
        self.assertEqual(1, tree.Count())
        self.assertEqual(2, tree.LeafCount())
        # 999 => [
        #   1 => [3],
        #   2
        # ]
        #
        tree.AddChild(root_node_one, parent_root_node_one)
        self.assertEqual(2, tree.Count())
        self.assertEqual(2, tree.LeafCount())
        # 999 => [
        #   1 => [3],
        #   2 => [4]
        # ]
        tree.AddChild(root_node_two, parent_root_node_two)
        self.assertEqual(3, tree.Count())
        self.assertEqual(2, tree.LeafCount())
        root_node_three = SimpleTreeNode(5, None)
        tree.AddChild(main_node, root_node_three)
        # 999 => [
        #   1 => [3],
        #   2 => [4],
        #   5
        # ]
        self.assertEqual(3, tree.Count())
        self.assertEqual(3, tree.LeafCount())
        tree.AddChild(parent_root_node_two, parent_root_node_two_child)
        # 999 => [
        #   1 => [3],
        #   2 => [4 => [10]],
        #   5
        # ]
        self.assertEqual(4, tree.Count())
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

        root_node_forth = SimpleTreeNode(10, None)
        root_node_forth_child_1 = SimpleTreeNode(11, None)
        root_node_forth_child_2 = SimpleTreeNode(12, None)
        root_node_forth_child_1_child_1 = SimpleTreeNode(112, None)

        # 999 -> [1 -> [3],2 -> [4], 5, 10 => [11, 12 => [112]]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(main_node, root_node_forth)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)
        tree.AddChild(root_node_forth, root_node_forth_child_1)
        tree.AddChild(root_node_forth, root_node_forth_child_2)
        tree.AddChild(root_node_forth_child_2, root_node_forth_child_1_child_1)

        # 999 -> [1 -> [3], 5, 10 => [11, 12 => [112]]
        tree.DeleteNode(root_node_two)
        self.assertEqual(3, len(main_node.Children))
        self.assertEqual(5, main_node.Children[0].NodeValue)
        self.assertEqual(1, main_node.Children[1].NodeValue)

        # 999 -> [5, 10 => [11, 12 => [112]]
        tree.DeleteNode(root_node_one)
        self.assertEqual(2, len(main_node.Children))
        self.assertEqual(5, main_node.Children[0].NodeValue)

        # 999 -> [5, 10 => [11]]
        tree.DeleteNode(root_node_forth_child_2)
        five = main_node.Children[0]
        ten = main_node.Children[1]
        self.assertEqual(2, len(main_node.Children))
        self.assertEqual(5, five.NodeValue)
        self.assertEqual(10, ten.NodeValue)
        self.assertEqual(0, len(five.Children))
        self.assertEqual(1, len(ten.Children))
        self.assertEqual(11, ten.Children[0].NodeValue)

        # 999 -> [5]
        tree.DeleteNode(root_node_forth)
        self.assertEqual(1, len(main_node.Children))
        five = main_node.Children[0]
        self.assertEqual(0, len(five.Children))
        self.assertEqual(5, five.NodeValue)

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

        two = tree.Root.Children[2]  # 2
        self.assertEqual(2, two.NodeValue)
        self.assertEqual(0, len(two.Children))

    def test_calc_depth(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        parent_root_node_two_child = SimpleTreeNode(10, None)
        # 999 => [1]
        tree.AddChild(main_node, root_node_one)
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        # 999 => [1, 2]
        tree.AddChild(main_node, root_node_two)
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        self.assertEqual(1, root_node_two.Level)
        # 999 => [
        #   1 => [3],
        #   2
        # ]
        #
        tree.AddChild(root_node_one, parent_root_node_one)
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        self.assertEqual(1, root_node_two.Level)
        self.assertEqual(2, parent_root_node_one.Level)
        # 999 => [
        #   1 => [3],
        #   2 => [4]
        # ]
        tree.AddChild(root_node_two, parent_root_node_two)
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        self.assertEqual(1, root_node_two.Level)
        self.assertEqual(2, parent_root_node_one.Level)
        self.assertEqual(2, parent_root_node_two.Level)
        root_node_three = SimpleTreeNode(5, None)

        # 999 => [
        #   1 => [3],
        #   2 => [4 => [10]],
        #   5
        # ]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(parent_root_node_two, parent_root_node_two_child)
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        self.assertEqual(1, root_node_two.Level)
        self.assertEqual(1, root_node_three.Level)
        self.assertEqual(2, parent_root_node_one.Level)
        self.assertEqual(2, parent_root_node_two.Level)
        self.assertEqual(3, parent_root_node_two_child.Level)
        # пересчитали дерево, должны получить тоже самое

        main = tree.Root
        self.assertEqual(999, main.NodeValue)
        self.assertTrue(main.HasChildren())
        children = main.Children
        self.assertEqual(3, len(children))
        [first, second, third] = children
        self.assertEqual(1, first.NodeValue)
        self.assertEqual(2, second.NodeValue)
        self.assertEqual(5, third.NodeValue)
        self.assertEqual(1, len(first.Children))
        self.assertEqual(1, len(second.Children))
        self.assertEqual(0, len(third.Children))
        self.assertEqual(3, first.Children[0].NodeValue)
        self.assertFalse(first.Children[0].HasChildren())
        forth = second.Children[0]
        self.assertEqual(4, forth.NodeValue)
        self.assertTrue(forth.HasChildren())
        self.assertEqual(10, forth.Children[0].NodeValue)
        self.assertFalse(forth.Children[0].HasChildren())

    def test_calc_depth_refresh(self):
        tree = SimpleTree(None)
        main_node = SimpleTreeNode(999, None)
        tree.AddChild(None, main_node)
        root_node_one = SimpleTreeNode(1, None)
        parent_root_node_one = SimpleTreeNode(3, None)
        root_node_two = SimpleTreeNode(2, None)
        parent_root_node_two = SimpleTreeNode(4, None)
        parent_root_node_two_child = SimpleTreeNode(10, None)
        tree.AddChild(main_node, root_node_one)
        tree.AddChild(main_node, root_node_two)
        tree.AddChild(root_node_one, parent_root_node_one)
        tree.AddChild(root_node_two, parent_root_node_two)
        root_node_three = SimpleTreeNode(5, None)
        #
        # # 999 => [
        # #   1 => [3],
        # #   2 => [4 => [10]],
        # #   5
        # # ]
        tree.AddChild(main_node, root_node_three)
        tree.AddChild(parent_root_node_two, parent_root_node_two_child)
        # # пересчитали дерево, должны получить тоже самое
        tree.CalcDepthLevel()
        self.assertEqual(0, main_node.Level)
        self.assertEqual(1, root_node_one.Level)
        self.assertEqual(1, root_node_two.Level)
        self.assertEqual(1, root_node_three.Level)
        self.assertEqual(2, parent_root_node_one.Level)
        self.assertEqual(2, parent_root_node_two.Level)
        self.assertEqual(3, parent_root_node_two_child.Level)