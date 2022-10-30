import random


def generate_balance_parentheses(count: int) -> str:
    """Генерация сбалансированных скобок"""
    if count < 1:
        raise ArithmeticError("Count must be positive")

    return add_balance_parenthes(count, '')


def add_balance_parenthes(count: int, _input: str) -> str:
    length = len(_input)
    if length / 2 == count:
        return _input

    max_position = length - 1 if length > 1 else 0
    random_position = random.randint(0, max_position)

    before = _input[:random_position]
    after = _input[random_position:]

    return add_balance_parenthes(count, before + '()' + after)
