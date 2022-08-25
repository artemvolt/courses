class AbstractNode:
    def __init__(self, v=None):
        self.value = v
        self.prev = None
        self.next = None


class Node(AbstractNode):
    def __init__(self, v):
        super().__init__(v)


class DummyNode(AbstractNode):
    def __init__(self):
        super().__init__()


# noinspection PyPep8Naming,PyPep8,PyMethodMayBeStatic,PyShadowingBuiltins,PyUnusedLocal
class LinkedList2WithDummy:
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        if isinstance(item, DummyNode):
            raise TypeError("Invalid type of item")
        prev = self.tail.prev
        prev.next = item
        item.prev = prev
        item.next = self.tail
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while node is not None:
            if isinstance(node, DummyNode):
                node = node.next
                continue

            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        result = []
        node = self.head.next
        while node is not None:
            if isinstance(node, DummyNode):
                node = node.next
                continue

            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        node = self.head.next
        head = self.head.next
        tail = self.tail.prev
        if head is None:
            return
        if head == tail and head.value == val:
            self.head.next = None
            self.tail.prev = None
            return

        while node is not None:
            if isinstance(node, DummyNode):
                node = node.next
                continue

            if node.value == val:
                prev = node.prev
                next = node.next

                prev.next = next
                next.prev = prev
                if all is True:
                    node = node.next
                    continue
                else:
                    return

            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        node = self.head.next
        count = 0
        while node is not None:
            if isinstance(node, DummyNode):
                node = node.next
                continue

            currentNode = node
            node = node.next
            count += 1

        return count

    def insert(self, afterNode, newNode):
        if isinstance(newNode, DummyNode) or isinstance(afterNode, DummyNode):
            raise TypeError("Invalid type of newNode")

        node = self.head.next
        if afterNode is None:
            self.add_in_tail(newNode)
            return

        while node is not None:
            if isinstance(node, DummyNode):
                node = node.next
                continue

            if node.value == afterNode.value:
                next = afterNode.next
                afterNode.next = newNode
                newNode.next = next
                newNode.prev = afterNode
                next.prev = newNode
                return

            node = node.next

    def add_in_head(self, newNode):
        if isinstance(newNode, DummyNode):
            raise TypeError("Invalid type of item")

        if self.head.next is None:
            self.head.next = newNode
            self.tail.prev = newNode
            newNode.prev = self.head
            newNode.next = self.tail
            return

        next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = next
        next.prev = newNode
