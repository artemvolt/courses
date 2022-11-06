class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

    def HasChildren(self):
        return len(self.Children) > 0

    def AddChildren(self, NewChildren):
        self.Children.append(NewChildren)

    def isEqualValue(self, value):
        return self.NodeValue == value

    def isEqualChildren(self, CompareValue):
        if len(self.Children) != len(CompareValue.Children):
            return False

        for children in self.Children:
            for children_compare in CompareValue.Children:
                if children.isEqualValue(children_compare.NodeValue) is False:
                    return False

        return True

    def isEqual(self, CompareNode):
        return self.isEqualValue(CompareNode.NodeValue) and \
               self.Parent.NodeValue == CompareNode.Parent.NodeValue and \
               self.isEqualChildren(CompareNode)


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        if ParentNode is None:
            NewChild.Parent = None
            self.Root = NewChild
        else:
            NewChild.Parent = ParentNode
            ParentNode.AddChildren(NewChild)

    def DeleteNode(self, NodeToDelete):
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

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        if self.Root is None:
            return []

        return self.GetAllNodesInNode(self.Root)

    def GetAllNodesInNode(self, Node):
        nodes = []
        if Node.HasChildren():
            nodes.append(Node)

            for children in Node.Children:
                nodes = nodes + self.GetAllNodesInNode(children)

        return nodes

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        if self.Root is None:
            return []

        return self.FindNodesByValueInNode(val, self.Root)

    def FindNodesByValueInNode(self, val, Node):
        nodes = []
        if Node.HasChildren():
            if Node.isEqualValue(val):
                nodes.append(Node)

            for children in Node.Children:
                nodes = nodes + self.FindNodesByValueInNode(val, children)

        return nodes

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        current_parent = OriginalNode.Parent
        parent_children = current_parent.Children
        for children in parent_children:
            if children.isEqualValue(OriginalNode.NodeValue):
                parent_children.remove(children)

        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        # количество всех узлов в дереве
        if self.Root is None:
            return 0

        if self.Root.HasChildren() is False:
            return 0

        count = 1
        for child in self.Root.Children:
            count += self.Count_Node(child)

        return count

    def Count_Node(self, Node):
        count = 0
        if Node.HasChildren() is True:
            count = 1
            for child in Node.Children:
                count += self.Count_Node(child)

        return count

    def LeafCount(self):
        # количество листьев в дереве
        if self.Root is None:
            return 0

        if self.Root.HasChildren() is False:
            return 1

        count = 0
        for child in self.Root.Children:
            count += self.LeafCountNode(child)

        return count

    def LeafCountNode(self, Node):
        count = 0
        if Node.HasChildren() is True:
            for child in Node.Children:
                count += self.LeafCountNode(child)
        else:
            count += 1

        return count

    def Print(self):
        if self.Root is None:
            return

        self.PrintNode(self.Root)

    def PrintNode(self, Node):
        print(" ==== ")
        print("node: ", Node.NodeValue)
        parent = Node.Parent
        if parent is not None:
            print('parent: ', parent.NodeValue)
        for children in Node.Children:
            self.PrintNode(children)
