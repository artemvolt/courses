class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


# noinspection PyComparisonWithNone,Pylint,PyPep8
class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0

        return 1 if v1 > v2 else -1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.__ascending == (self.compare(new_node.value, self.head.value) < 0):
            head = self.head
            self.head = new_node
            new_node.next = head
            head.prev = new_node
            return

        if self.__ascending == (self.compare(new_node.value, self.tail.value) >= 0):
            tail = self.tail
            new_node.prev = tail
            tail.next = new_node
            self.tail = new_node
            return

        node = self.head
        while next is not None:
            if self.__ascending:
                if self.compare(new_node.value, node.value) >= 0 and self.compare(new_node.value, node.next.value) <= 0:
                    current = node
                    current_next = node.next
                    current.next = new_node
                    new_node.prev = current
                    new_node.next = current_next
                    current_next.prev = new_node
                    break

            if not self.__ascending:
                if self.compare(new_node.value, node.value) <= 0 and self.compare(new_node.value, node.next.value) >= 0:
                    current = node
                    current_next = node.next
                    current.next = new_node
                    new_node.prev = current
                    new_node.next = current_next
                    current_next.prev = new_node
                    break

            node = node.next
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            if self.__ascending is True and (self.compare(node.value, val) > 0):
                return None
            if self.__ascending is False and (self.compare(node.value, val) < 0):
                return None
            node = node.next
        return None  # здесь будет ваш код

    def delete(self, val):
        node = self.head
        if node is None:
            return
        if self.len() == 1:
            if node.value == val:
                self.clean(self.__ascending)
            return

        while node is not None:
            prev = node.prev
            next = node.next

            if node.value == val:
                # head
                if prev is None:
                    self.head = next
                    next.prev = None
                    node = node.next
                    break

                # tail
                if next is None:
                    self.tail = prev
                    prev.next = None
                    node = node.next
                    break

                prev.next = next
                next.prev = prev
                break

            node = node.next
        # здесь будет ваш код

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        # здесь будет ваш код

    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count  # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


# noinspection PyCompatibility
class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        return super().compare(v1.strip(), v2.strip())
