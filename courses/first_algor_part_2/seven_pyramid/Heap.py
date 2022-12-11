class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a: list, depth: int):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for value in a:
            self.Add(value)
        pass

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if len(self.HeapArray) == 0:
            return -1

        value = self.HeapArray[0]
        if value is None:
            return -1  # если куча пуста

        try:
            last_index = self.HeapArray.index(None) - 1
            value_for_move = self.HeapArray[last_index]
        except ValueError:
            last_index = len(self.HeapArray) - 1
            value_for_move = self.HeapArray[last_index]

        self.HeapArray[last_index] = None
        self.HeapArray[0] = value_for_move
        current_index = 0

        while current_index >= 0:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            left_child_value = self.HeapArray[left_child_index]
            right_child_value = self.HeapArray[right_child_index]
            current_value = self.HeapArray[current_index]
            max_index = None

            if left_child_value is None and right_child_value is None:
                break

            if left_child_value is None or right_child_value is None:
                if left_child_value is None and right_child_value is not None:
                    max_index = right_child_index
                if right_child_value is None and left_child_value is not None:
                    max_index = left_child_index
            else:
                if left_child_value > right_child_value:
                    max_index = left_child_index
                if right_child_value > left_child_value:
                    max_index = right_child_index

            max_index_value = self.HeapArray[max_index]
            if current_value > max_index_value:
                break
            if current_value < max_index_value:
                self.HeapArray[max_index] = current_value
                self.HeapArray[current_index] = max_index_value
                current_index = max_index

        return value

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if None not in self.HeapArray:
            return False  # если куча вся заполнена

        last_for_insert_index = self.HeapArray.index(None)
        self.HeapArray[last_for_insert_index] = key
        if last_for_insert_index == 0:
            return

        compare_index = last_for_insert_index
        while compare_index > 0:
            item_value = self.HeapArray[compare_index]
            parent_index = (compare_index - 1) // 2
            parent_value = self.HeapArray[parent_index]

            if item_value > parent_value:
                self.HeapArray[compare_index] = parent_value
                self.HeapArray[parent_index] = item_value

            compare_index = parent_index

        return True
