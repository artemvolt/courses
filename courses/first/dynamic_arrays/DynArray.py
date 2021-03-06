import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    # noinspection PyMethodMayBeStatic
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # добавляем объект itm в позицию i, начиная с 0
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if i == self.count:
            self.append(itm)
            return

        if len(self) == 0:
            self.array[i] = itm
            self.count += 1
            return

        size = self.capacity
        if self.count == self.capacity:
            size *= 2
            self.resize(size)

        current = None
        for k in range(i, self.count):
            if current is None:
                current = self.array[k]
                self.array[k] = itm
            else:
                current_save = self.array[k]
                self.array[k] = current
                current = current_save
                if k == (self.count - 1):
                    self.array[k + 1] = current

        self.count += 1

    def delete(self, i):
        # удаляем объект в позиции i
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == 0:
            raise IndexError('You cannot delete in empty array')

        for k in range(i, self.count - 1):
            self.array[k] = self.array[k + 1]

        self.count -= 1

        if self.capacity > 16:
            if self.count < (self.capacity / 2):
                result_cap = int(self.capacity / 1.5)
                if result_cap < 16:
                    self.resize(16)
                else:
                    self.resize(result_cap)
