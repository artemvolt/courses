class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


# noinspection PyPep8Naming,PyPep8,PyMethodMayBeStatic,PyShadowingBuiltins,PyUnusedLocal
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        if self.head is not None and self.head.value == val:
            return self.head
        if self.tail is not None and self.tail.value == val:
            return self.tail

        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if self.head is None:
            return

        if self.head.value == val and self.tail == self.head:
            self.head = None
            self.tail = None
            return

        node = self.head
        while node is not None:
            # head
            if node.value == val:
                # head of list
                if node == self.head:
                    next = self.head.next
                    next.prev = None
                    self.head = next

                    if all is True:
                        node = self.head.next
                        continue
                    return

                # end of list
                if node == self.tail:
                    prev = self.tail.prev
                    prev.next = None
                    self.tail = prev
                    return

                prev_node = node.prev
                prev_node.next = node.next
                node = node.next

                if all is False:
                    return

            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        if afterNode is None and self.head is not None and self.tail is not None:
            self.add_in_tail(newNode)
            return

        node = self.head
        while node is not None:
            # end of list
            if node.value == afterNode.value:
                if self.tail == afterNode:
                    afterNode.next = newNode
                    newNode.prev = afterNode
                    self.tail = newNode
                    return
                if self.head == afterNode:
                    newNode.prev = self.head
                    if self.head is not None:
                        newNode.next = self.head.next
                    if newNode.next is not None:
                        newNode.next.prev = newNode
                    self.head.next = newNode
                    return

                newNode.prev = afterNode
                newNode.next = afterNode.next
                if newNode.next is not None:
                    newNode.next.prev = newNode
                afterNode.next = newNode
                return

            node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        head = self.head
        newNode.next = head
        head.prev = newNode
        self.head = newNode
