class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1

    def hash_fun(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return abs(hash % self.size)

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        while True:
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                break
            if self.slots[index] == key:
                self.values[index] = value
                break

            index = (index + self.step) % self.size

    def get(self, key):
        if key in self.slots:
            return self.values[self.slots.index(key)]
        return None
