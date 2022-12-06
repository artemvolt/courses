class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a: list):
        if len(a) > 0:
            a_sorted = sorted(a)
            self.Root = self.GenerateTreeRecursive(a_sorted, node_parent=None, level=0)

        return self

    def GenerateTreeRecursive(self, sorted_array: list, node_parent, level: int) -> BSTNode:
        middle_index = len(sorted_array) // 2
        node = BSTNode(sorted_array[middle_index], node_parent)
        node.Level = level
        if len(sorted_array) > 1:
            next_level = level + 1
            left_subtree = sorted_array[:middle_index]
            if len(left_subtree) > 0:
                node.LeftChild = self.GenerateTreeRecursive(left_subtree, node, next_level)

            right_subtree = sorted_array[middle_index + 1:]
            if len(right_subtree) > 0:
                node.RightChild = self.GenerateTreeRecursive(right_subtree, node, next_level)
        return node

    def IsBalanced(self, root_node) -> bool:
        if root_node is None:
            return True

        [is_balance, level] = self.IsBalancedRecursive(root_node)
        return is_balance

    def IsBalancedRecursive(self, sub_root: BSTNode) -> list:
        if sub_root is None:
            return [True, 0]
        [left_balanced, left_level] = self.IsBalancedRecursive(sub_root.LeftChild)
        [right_balanced, right_level] = self.IsBalancedRecursive(sub_root.RightChild)
        is_balanced = left_balanced and right_balanced and abs(left_level - right_level) <= 1
        return [is_balanced, max(left_level, right_level) + 1]