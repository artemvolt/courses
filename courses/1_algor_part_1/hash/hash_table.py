class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = 0
        for char in value:
            hash += ord(char)

        return abs(hash % self.size)

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index

        checked = []
        while True:
            index = (index + self.step) % self.size
            checked.append(index)
            if self.slots[index] is None:
                return index

            if len(checked) == len(self.slots):
                return None

    def put(self, value):
        index = self.seek_slot(value)
        if not index is None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index

        checked = []
        while True:
            index = (index + self.step) % self.size
            checked.append(index)
            if self.slots[index] == value:
                return index

            if len(checked) == len(self.slots):
                return None
        # находит индекс слота со значением, или None
