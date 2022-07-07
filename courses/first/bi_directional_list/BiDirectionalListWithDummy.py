class AbstractNode:
    def __init__(self, is_dummy, v=None):
        self.value = v
        self.prev = None
        self.next = None
        self.is_dummy = is_dummy


class Node(AbstractNode):
    def __init__(self, v):
        super().__init__(False, v)


class DummyNode(AbstractNode):
    def __init__(self):
        super().__init__(True)


# noinspection PyPep8Naming,PyPep8,PyMethodMayBeStatic,PyShadowingBuiltins,PyUnusedLocal
class LinkedList2WithDummy:
    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        prev = self.tail.prev
        prev.next = item
        item.prev = prev
        item.next = self.tail
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        result = []
        node = self.head.next
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        node = self.head
        head = self.head.next
        tail = self.tail.prev
        if head is None:
            return
        if head == tail and head.value == val:
            self.head.next = None
            self.tail.prev = None
            return

        while node is not None:
            if node.is_dummy:
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
        node = self.head
        count = 0
        while node is not None:
            currentNode = node
            if currentNode.is_dummy is False:
                count += 1
            node = node.next

        return count

    def insert(self, afterNode, newNode):

        node = self.head
        if afterNode is None:
            self.add_in_tail(newNode)
            return

        while node is not None:
            if node.is_dummy:
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
