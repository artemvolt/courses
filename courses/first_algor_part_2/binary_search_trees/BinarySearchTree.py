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
        self.count = 0

    def FindNodeByKeyRecursive(self, key, node: BSTNode) -> BSTFind:
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

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root is None:
            return BSTFind()
        return self.FindNodeByKeyRecursive(key, self.Root)

    def AddKeyValue(self, key, val) -> bool:
        # добавляем ключ-значение в дерево
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
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        right = FromNode.RightChild
        left = FromNode.LeftChild
        node = right if FindMax is True else left
        if node is None:
            return FromNode
        return self.FinMinMax(node, FindMax)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        found = self.FindNodeByKey(key)
        if found.NodeHasKey and found.Node is not None:
            node = found.Node
            parent = node.Parent
            new_node = self.FinMinMax(node, True)
            if node is new_node:
                if parent is not None:
                    if node is parent.LeftChild:
                        parent.LeftChild = None
                    if node is parent.RightChild:
                        parent.RightChild = None
                else:
                    self.Root = None
                return True
            elif parent is None:
                self.Root = new_node
                return True

            if node is parent.LeftChild:
                parent.LeftChild = new_node
                return True
            if node is parent.RightChild:
                parent.RightChild = new_node
                return True
        return False  # если узел не найден

    def Count(self) -> int:
        self.count = 0
        self.Count_Recursive(self.Root)
        return self.count

    def Count_Recursive(self, node):
        if node is None:
            return self.count
        self.count += 1
        if node.LeftChild is not None:
            self.Count_Recursive(node.LeftChild)
        if node.RightChild is not None:
            self.Count_Recursive(node.RightChild)
