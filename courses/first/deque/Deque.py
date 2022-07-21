# noinspection PyPep8Naming,PyMissingOrEmptyDocstring
class Deque:
    def __init__(self):
        # инициализация внутреннего хранилища
        self.stack = []
        pass

    def addFront(self, item):
        # добавление в голову
        self.stack.insert(0, item)

    def addTail(self, item):
        # добавление в хвост
        self.stack.append(item)

    def removeFront(self):
        # удаление из головы
        if self.size() > 0:
            return self.stack.pop(0)
        return None  # если очередь пуста

    def removeTail(self):
        if self.size() > 0:
            return self.stack.pop()
        return None  # если очередь пуста

    def size(self):
        return len(self.stack)  # размер очереди
