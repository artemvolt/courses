# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.values = []

    def size(self):
        return len(self.values)
        # количество элементов в множестве

    def put(self, value):
        if not value in self.values:
            self.values.append(value)

    def get(self, value):
        return value in self.values

    def remove(self, value):
        if self.get(value):
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        set_new = PowerSet()
        bigger = self if self.size() >= set2.size() else set2
        smaller = set2 if self.size() >= set2.size() else self
        for el in smaller.values:
            if bigger.get(el):
                set_new.put(el)

        return set_new

    def union(self, set2):
        # объединение текущего множества и set2
        set_new = PowerSet()
        for el in self.values:
            set_new.put(el)

        for el2 in set2.values:
            set_new.put(el2)

        return set_new

    def difference(self, set2):
        set_new = PowerSet()
        for el in self.values:
            if set2.get(el) is False:
                set_new.put(el)
        # разница текущего множества и set2
        return set_new

    def issubset(self, set2):
        if self.size() >= set2.size():
            for el in set2.values:
                if not self.get(el):
                    return False
            return True
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False
