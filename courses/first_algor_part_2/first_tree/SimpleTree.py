# noinspection PyPep8Naming
class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
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
        self.Root = root

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        """
        add child to parent. If Parent is none, it's mean new child will be root node.
        :param ParentNode: SimpleTreeNode|None
        :param NewChild: SimpleTreeNode
        """
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
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self) -> list:
        """
        get all nodes in three
        :return: list
        """
        if self.Root is None:
            return []

        return self.GetAllNodesInNode(self.Root)

    def GetAllNodesInNode(self, Node: SimpleTreeNode) -> list:
        """
        get all nodes in node recursive
        :param Node: SimpleTreeNode
        :return: list
        """
        nodes = [Node]

        for children in Node.Children:
            nodes = nodes + self.GetAllNodesInNode(children)

        return nodes

    def FindNodesByValue(self, val) -> list:
        """
        find all nodes by value in three
        :param val:
        :return: list
        """
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
        if NewParent is None:
            self.Root = OriginalNode
            OriginalNode.Parent = None
            self.CalcDepthLevel()
            return

        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
        self.CalcDepthLevelNode(OriginalNode)

    def Count(self) -> int:
        """
        calc count nodes of three
        :return: int
        """
        return self.Count_Node(self.Root)

    def Count_Node(self, Node: SimpleTreeNode) -> int:
        """
        calc count node recursive
        :param Node: SimpleTreeNode
        :return: int
        """
        count = 0
        if Node is not None:
            count += 1
            for child in Node.Children:
                count += self.Count_Node(child)

        return count

    def LeafCount(self) -> int:
        """
        calc count for all leafs in tree
        :return: int
        """
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
