class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.stack = []

    def enqueue(self, item):
        # вставка в хвост
        self.stack.append(item)

    def dequeue(self):
        # выдача из головы
        if self.size() > 0:
            return self.stack.pop(0)
        return None  # если очередь пустая

    def size(self):
        return len(self.stack)  # размер очереди

    def rotate(self, count):
        if self.size() == 0:
            return

        while count > 0:
            self.enqueue(self.dequeue())
            count -= 1

