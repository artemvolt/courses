from tokenize import String
import operator
import sys

from courses.first.stack.Stack import Stack

sys.path.append('/var/www/courses')


def postfix_calc(input_raw: String) -> String:
    if len(input_raw) == 0:
        raise AttributeError("Передана на вход пустая строка")

    numbers_stack = Stack()
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }

    for el in input_raw:
        if el in ops:
            if not numbers_stack.size() == 2:
                raise AttributeError("Для операции необходимо два операнда")

            func_math = ops[el]
            first = numbers_stack.pop()
            second = numbers_stack.pop()
            result = func_math(second, first)
            numbers_stack.push(result)

        if el.isdigit():
            numbers_stack.push(int(el))

        if el == '=':
            return numbers_stack.peek()

    return None
