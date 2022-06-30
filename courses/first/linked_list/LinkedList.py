class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = list()
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)

            node = node.next
        return result

    def delete(self, val, all=False):
        head = self.head
        prev = None

        count = 0
        countStop = self.head
        while countStop is not None:
            count += 1
            countStop = countStop.next

        if count == 0:
            return

        if count == 1 and self.head.value == val:
            self.head = None
            self.tail = None
            return

        while head is not None:
            if head.value == val:
                if head == self.head:
                    self.head = head.next
                    prev = None
                    head = head.next

                    if not all:
                        head = None

                    continue

                if head == self.tail:
                    prev.next = None
                    self.tail = prev
                    prev = head
                    head = None

                    if not all:
                        head = None

                    continue

                prev.next = head.next
                prev = prev
                head = head.next
                if not all:
                    head = None
            else:
                prev = head
                head = head.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node != None:
            length += 1
            node = node.next

        return length

    def insert(self, afterNode, newNode):
        pass  # здесь будет ваш код
