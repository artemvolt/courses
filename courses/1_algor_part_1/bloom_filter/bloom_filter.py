class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.bit_mask = 0

    def calc_hash(self, _input, number):
        hash = 0
        for letter in _input:
            code = ord(letter)
            hash = ((hash * number) + code) % self.filter_len

        return 1 << hash

    def hash1(self, str1):
        # 17
        return self.calc_hash(str1, 17)

    def hash2(self, str1):
        # 223
        return self.calc_hash(str1, 223)

    def add(self, str1):
        # добавляем строку str1 в фильтр
        self.bit_mask = self.bit_mask | self.hash1(str1)
        self.bit_mask = self.bit_mask | self.hash2(str1)

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        return self.bit_mask & self.hash1(str1) != 0 and \
               self.bit_mask & self.hash2(str1) != 0
