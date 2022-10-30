import random


def balance_parentheses(count: int) -> str:
    """Генерация сбалансированных скобок"""
    if count < 1:
        raise ArithmeticError("Count must be positive")

    list = ['(', ')']
    for i in range(0, count):
        random_position = random.choice(get_indexes(list))
        list.insert(random_position, ')')
        list.insert(random_position, '(')

    return ''.join(map(lambda item: item, list))


def get_indexes(_input: list) -> list:
    """Получить индексы массива"""
    result = []
    for index, value in enumerate(_input):
        result.append(index)
    return result
