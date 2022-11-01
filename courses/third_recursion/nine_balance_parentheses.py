import random
import time


def generate_balance_parentheses(count: int) -> str:
    """Генерация сбалансированных скобок"""
    if count < 1:
        raise ArithmeticError("Count must be positive")

    return add_balance_parenthes(count, '')


def add_balance_parenthes(count: int, _input: str) -> str:
    length = len(_input)
    if length / 2 == count:
        print(_input)
        return _input

    max_position = length - 1 if length > 1 else 0
    current_time = time.time()
    current_time_int = int(current_time)
    diff_time = current_time - current_time_int

    # 5 знак после запятой меняется чаще, чем ближайшие
    multiply_five = diff_time * (10**5)
    multiply_five_int = int(multiply_five)

    # получаем это число
    diff_multiply_five = multiply_five - multiply_five_int
    diff_int = int(diff_multiply_five * 10)

    random_position = max_position if diff_int > max_position else diff_int

    before = _input[:random_position]
    after = _input[random_position:]

    return add_balance_parenthes(count, before + '()' + after)
