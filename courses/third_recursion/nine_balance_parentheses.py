import random


def balance_parentheses(count: int) -> str:
    """Генерация сбалансированных скобок"""
    if count < 1:
        raise ArithmeticError("Count must be positive")

    return add_balance(count, '')


def add_balance(count: int, _input: str) -> str:
    length = len(_input)
    if length / 2 == count:
        return _input

    max_index = length - 1 if length > 1 else 0
    random_index = random.randint(0, max_index)

    before = _input[:random_index]
    after = _input[random_index:]

    return add_balance(count, before + '()' + after)
