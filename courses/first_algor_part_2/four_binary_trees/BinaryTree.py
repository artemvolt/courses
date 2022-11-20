class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2**depth + 2**depth - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if len(self.Tree) > 0:
            return self.FindKeyIndexRecursive(key, 0)
        return None  # не найден

    def FindKeyIndexRecursive(self, key, index):
        # ищем в массиве индекс ключа
        if self.Tree[index] == key:
            return index
        if self.Tree[index] is None:
            return -index

        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2

        if key < self.Tree[index] and leftChildIndex < len(self.Tree):
            return self.FindKeyIndexRecursive(key, leftChildIndex)
        if key > self.Tree[index] and rightChildIndex < len(self.Tree):
            return self.FindKeyIndexRecursive(key, rightChildIndex)

        return None  # не найден

    def AddKey(self, key):
        # добавляем ключ в массив
        existing = self.FindKeyIndex(key)
        if existing is None:
            return -1

        if existing < 0 or (existing == 0 and self.Tree[0] is None):
            self.Tree[abs(existing)] = key

        return abs(existing)
        # индекс добавленного/существующего ключа или -1 если не удалось