from courses.first.stack.Stack import Stack


class QueueStack:
    def __init__(self):
        # инициализация хранилища данных
        self.stack = Stack()

    def enqueue(self, item):
        # вставка в хвост
        reverse = Stack()
        for k in range(self.stack.size()):
            reverse.push(self.stack.pop())

        reverse.push(item)

        reverse_result = Stack()
        for k in range(reverse.size()):
            reverse_result.push(reverse.pop())

        self.stack = reverse_result

    def dequeue(self):
        # выдача из головы
        if self.size() > 0:
            return self.stack.pop()
        return None  # если очередь пустая

    def size(self):
        return self.stack.size()

    def rotate(self, count):
        if self.size() == 0:
            return

        while count > 0:
            self.enqueue(self.dequeue())
            count -= 1

