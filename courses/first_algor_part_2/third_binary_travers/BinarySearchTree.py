class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node: BSTNode = None):
        self.Root = node  # корень дерева, или None

    def FindNodeByKeyRecursive(self, key, node: BSTNode) -> BSTFind:
        """

        :param key:
        :param node: BSTNode
        :return: BSTFind
        """
        if key < node.NodeKey and node.LeftChild is not None:
            return self.FindNodeByKeyRecursive(key, node.LeftChild)

        if key > node.NodeKey and node.RightChild is not None:
            return self.FindNodeByKeyRecursive(key, node.RightChild)

        result = BSTFind()
        result.Node = node
        if key == node.NodeKey:
            result.NodeHasKey = True

        if key < node.NodeKey:
            result.ToLeft = True

        return result

    def FindNodeByKey(self, key) -> BSTFind:
        """

        :param key:
        :return: BSTFind
        """
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root is None:
            return BSTFind()
        return self.FindNodeByKeyRecursive(key, self.Root)

    def AddKeyValue(self, key, val) -> bool:
        """

        :param key:
        :param val:
        :return: bool
        """
        found = self.FindNodeByKey(key)
        if found.NodeHasKey:
            return False

        node = found.Node
        new = BSTNode(key, val, node)
        if node is None:
            self.Root = new
        elif found.ToLeft is True:
            node.LeftChild = new
        else:
            node.RightChild = new

        return True  # если ключ уже есть

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        """

        :param FromNode: BSTNode
        :param FindMax: bool
        :return: BSTNode
        """
        right = FromNode.RightChild
        left = FromNode.LeftChild
        node = right if FindMax is True else left
        if node is None:
            return FromNode
        return self.FinMinMax(node, FindMax)

    def DeleteNodeByKey(self, key):
        """

        :param key:
        :return:
        """
        found = self.FindNodeByKey(key)
        if found.NodeHasKey is False:
            return False

        foundNode = found.Node
        if foundNode.LeftChild is None or foundNode.RightChild is None:
            self.balance_node(foundNode)
            return True

        parent = foundNode.Parent
        foundMin = self.FinMinMax(foundNode.RightChild, False)
        self.balance_node(foundMin)
        foundMin.LeftChild = foundNode.LeftChild
        foundMin.RightChild = foundNode.RightChild
        foundNode.LeftChild.Parent = foundMin

        if foundNode.RightChild is not None:
            foundNode.RightChild.Parent = foundMin

        foundMin.Parent = parent

        if parent is None:
            self.Root = foundMin
        elif foundMin.NodeKey < parent.NodeKey:
            parent.LeftChild = foundMin
        else:
            parent.RightChild = foundMin

        return True

    def balance_node(self, node: BSTNode):
        """
        Case when node does not have left or right child.
        :param node:
        """
        parent = node.Parent
        child = None

        if node.RightChild is not None:
            child = node.RightChild
        elif node.LeftChild is not None:
            child = node.LeftChild

        if parent is None:
            self.Root = child
        elif node.NodeKey < parent.NodeKey:
            parent.LeftChild = child
        else:
            parent.RightChild = child

        if child is not None:
            child.Parent = parent

    def Count(self) -> int:
        return self.Count_Recursive(self.Root)

    def Count_Recursive(self, node) -> int:
        """
        count nodes of tree recursive
        :param node:
        :return:
        """
        count = 0
        if node is None:
            return count

        count += 1

        if node.LeftChild is not None:
            count += self.Count_Recursive(node.LeftChild)
        if node.RightChild is not None:
            count += self.Count_Recursive(node.RightChild)

        return count

    def Print(self, node):
        """
        print nodes with parent
        :param node:
        """
        parent = None if node.Parent is None else node.Parent.NodeValue
        print('parent: ', parent, 'node:', node.NodeValue)
        if node.LeftChild is not None:
            self.Print(node.LeftChild)
        if node.RightChild is not None:
            self.Print(node.RightChild)

    def WideAllNodes(self) -> list:
        """

        :return: list
        """
        if self.Root is None:
            return []

        return [self.Root] + self.WideAllNodesRecursive([self.Root])

    def WideAllNodesRecursive(self, nodes: list) -> list:
        """

        :param nodes: list
        :return: list
        """
        result = []
        for node in nodes:
            if node.LeftChild is not None:
                result.append(node.LeftChild)
            if node.RightChild is not None:
                result.append(node.RightChild)

        if len(result) > 0:
            result += self.WideAllNodesRecursive(result)

        return result

    def DeepAllNodes(self, _type: int) -> list:
        """

        :param _type: int
        :return: list
        """
        if self.Root is None:
            return []

        # in order
        if _type == 0:
            return self.DeepAllNodesInOrder(_type, self.Root)

        # post order
        if _type == 1:
            return self.DeepAllNodesPostOrder(_type, self.Root)

        # pre order
        if _type == 2:
            return self.DeepAllNodesPreOrder(_type, self.Root)

    def DeepAllNodesInOrder(self, _type: int, node: BSTNode) -> list:
        """

        :param _type: int
        :param node: BSTNode
        :return: list
        """
        result = []

        if node.LeftChild is not None:
            result += self.DeepAllNodesInOrder(_type, node.LeftChild)

        result.append(node)

        if node.RightChild is not None:
            result += self.DeepAllNodesInOrder(_type, node.RightChild)

        return result

    def DeepAllNodesPostOrder(self, _type: int, node: BSTNode) -> list:
        """

        :param _type: int
        :param node: BSTNode
        :return: list
        """
        result = []

        if node.LeftChild is not None:
            self.DeepAllNodesPostOrder(_type, node.LeftChild)

        if node.RightChild is not None:
            self.DeepAllNodesPostOrder(_type, node.RightChild)

        result.append(node)

        return result

    def DeepAllNodesPreOrder(self, _type: int, node: BSTNode) -> list:
        """

        :param _type: int
        :param node: BSTNode
        :return: list
        """
        result = [node]

        if node.LeftChild is not None:
            self.DeepAllNodesPreOrder(_type, node.LeftChild)

        if node.RightChild is not None:
            self.DeepAllNodesPreOrder(_type, node.RightChild)

        return result
