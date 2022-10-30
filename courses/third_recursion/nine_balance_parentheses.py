import random


def balance_parentheses(count: int) -> str:
    """Генерация сбалансированных скобок"""
    if count < 1:
        raise ArithmeticError("Count must be positive")

    return add_balance(count, '()')


def add_balance(count: int, _input: str) -> str:
    if len(_input) / 2 == count:
        return _input

    to_list = list(_input)
    random_position = random.choice(get_indexes(to_list))
    to_list.insert(random_position, ')')
    to_list.insert(random_position, '(')

    return add_balance(count, ''.join(map(lambda x: x, to_list)))


def get_indexes(_input: list) -> list:
    """Получить индексы массива"""
    result = []
    for index, value in enumerate(_input):
        result.append(index)
    return result
