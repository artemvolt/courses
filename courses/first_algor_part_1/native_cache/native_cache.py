class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
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
        start_index = index
        while True:
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                self.hits[index] += 1
                break
            if self.slots[index] == key:
                self.values[index] = value
                self.hits[index] += 1
                break

            index = (index + self.step) % self.size
            if start_index == index:
                min_hit_index = self.hits.index(min(self.hits))
                self.slots[min_hit_index] = key
                self.values[min_hit_index] = value
                self.hits[min_hit_index] = 0
                break

    def get(self, key):
        if key in self.slots:
            index = self.slots.index(key)
            self.hits[index] += 1
            return self.values[index]
        return None
