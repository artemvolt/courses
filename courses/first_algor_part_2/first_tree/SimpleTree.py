# noinspection PyPep8Naming
class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.Level = 0

    def HasChildren(self) -> bool:
        """
        does have current node children
        :return: bool
        """
        return len(self.Children) > 0

    def AddChildren(self, NewChildren: 'SimpleTreeNode'):
        """
        Add children to current node
        :param NewChildren:
        """
        self.Children.append(NewChildren)

    def isEqualValue(self, compare_value) -> bool:
        """
        is equal value with compare value
        :param compare_value:
        :return:
        """
        return self.NodeValue == compare_value

    def isEqualChildren(self, CompareValue: 'SimpleTreeNode') -> bool:
        """
        Check equal by children
        :param CompareValue: SimpleTreeNode
        :return: bool
        """
        if len(self.Children) != len(CompareValue.Children):
            return False

        for children in self.Children:
            for children_compare in CompareValue.Children:
                if children.isEqualValue(children_compare.NodeValue) is False:
                    return False

        return True

    def isEqual(self, CompareNode: 'SimpleTreeNode') -> bool:
        """
        Check equal by value and children
        :param CompareNode: SimpleTreeNode
        :return: bool
        """
        return self.isEqualValue(CompareNode.NodeValue) and \
               self.Parent.NodeValue == CompareNode.Parent.NodeValue and \
               self.isEqualChildren(CompareNode)


# noinspection PyPep8Naming
class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        """
        add child to parent. If Parent is none, it's mean new child will be root node.
        :param ParentNode: SimpleTreeNode|None
        :param NewChild: SimpleTreeNode
        """
        # ваш код добавления нового дочернего узла существующему ParentNode
        if ParentNode is None:
            NewChild.Parent = None
            self.Root = NewChild
            self.CalcDepthLevelNode(NewChild)
        else:
            NewChild.Parent = ParentNode
            ParentNode.AddChildren(NewChild)
            self.CalcDepthLevelNode(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        """
        delete node in three
        :param NodeToDelete: SimpleTreeNode
        """
        # ваш код удаления существующего узла NodeToDelete
        all_nodes = self.GetAllNodes()
        for node in all_nodes:
            if node.isEqual(NodeToDelete):
                children = NodeToDelete.Children
                parent = node.Parent
                for child in children:
                    children.remove(child)

                for children_parent in parent.Children:
                    if children_parent.isEqual(node):
                        parent.Children.remove(children_parent)

    def GetAllNodes(self) -> list:
        """
        get all nodes in three
        :return: list
        """
        # ваш код выдачи всех узлов дерева в определённом порядке
        if self.Root is None:
            return []

        return self.GetAllNodesInNode(self.Root)

    def GetAllNodesInNode(self, Node: SimpleTreeNode) -> list:
        """
        get all nodes in node recursive
        :param Node: SimpleTreeNode
        :return: list
        """
        nodes = []
        if Node.HasChildren():
            nodes.append(Node)

            for children in Node.Children:
                nodes = nodes + self.GetAllNodesInNode(children)

        return nodes

    def FindNodesByValue(self, val) -> list:
        """
        find all nodes by value in three
        :param val:
        :return: list
        """
        # ваш код поиска узлов по значению
        if self.Root is None:
            return []

        return self.FindNodesByValueInNode(val, self.Root)

    def FindNodesByValueInNode(self, val, Node: SimpleTreeNode) -> list:
        """
        Find all nodes by value recursive
        :param val:
        :param Node: SimpleTreeNode
        :return: list
        """
        nodes = []
        if Node.HasChildren():
            if Node.isEqualValue(val):
                nodes.append(Node)

            for children in Node.Children:
                nodes = nodes + self.FindNodesByValueInNode(val, children)

        return nodes

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        """
        move original node to new parent
        :param OriginalNode: SimpleTreeNode
        :param NewParent: SimpleTreeNode
        :return:
        """
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        if NewParent is None:
            self.Root = OriginalNode
            OriginalNode.Parent = None
            self.CalcDepthLevel()
            return

        current_parent = OriginalNode.Parent
        parent_children = current_parent.Children
        for children in parent_children:
            if children.isEqualValue(OriginalNode.NodeValue):
                parent_children.remove(children)

        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)
        self.CalcDepthLevelNode(OriginalNode)

    def Count(self) -> int:
        """
        calc count nodes of three
        :return: int
        """
        # количество всех узлов в дереве
        if self.Root is None:
            return 0

        if self.Root.HasChildren() is False:
            return 0

        count = 1
        for child in self.Root.Children:
            count += self.Count_Node(child)

        return count

    def Count_Node(self, Node: SimpleTreeNode) -> int:
        """
        calc count node recursive
        :param Node: SimpleTreeNode
        :return: int
        """
        count = 0
        if Node.HasChildren() is True:
            count = 1
            for child in Node.Children:
                count += self.Count_Node(child)

        return count

    def LeafCount(self) -> int:
        """
        calc count for all leafs in tree
        :return: int
        """
        # количество листьев в дереве
        if self.Root is None:
            return 0

        if self.Root.HasChildren() is False:
            return 1

        count = 0
        for child in self.Root.Children:
            count += self.LeafCountNode(child)

        return count

    def LeafCountNode(self, Node: SimpleTreeNode) -> int:
        """
        Calc count for leaf recursive
        :param Node: SimpleTreeNode
        :return: int
        """
        count = 0
        if Node.HasChildren() is True:
            for child in Node.Children:
                count += self.LeafCountNode(child)
        else:
            count += 1

        return count

    def Print(self):
        """
        print tree
        :return:
        """
        if self.Root is None:
            return

        self.PrintNode(self.Root)

    def PrintNode(self, Node: SimpleTreeNode):
        """
        print each node with children recursive
        :param Node: SimpleTreeNode
        """
        print(" ==== ")
        print("node: ", Node.NodeValue)
        parent = Node.Parent
        if parent is not None:
            print('parent: ', parent.NodeValue)
        for children in Node.Children:
            self.PrintNode(children)

    def CalcDepthLevel(self):
        """
        set depth for each item of three
        """
        root = self.Root
        if root is not None:
            self.CalcDepthLevelNode(root)

    def CalcDepthLevelNode(self, node: SimpleTreeNode):
        """
        set level for each node recursive
        :param node: SimpleTreeNode
        """
        if node.Parent is None:
            node.Level = 0
        else:
            node.Level = node.Parent.Level + 1

        for child in node.Children:
            self.CalcDepthLevelNode(child)
