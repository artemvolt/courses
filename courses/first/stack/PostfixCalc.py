from tokenize import String

from courses.first.stack.Stack import Stack


def postfix_calc(input_raw: String):
    if len(input_raw) == 0:
        raise AttributeError("Передана на вход пустая строка")

    numbers_stack = Stack()

    for el in input_raw:
        if el == "+" or el == '*':
            if not numbers_stack.size() == 2:
                raise AttributeError("Для операции необходимо два операнда")
            if el == "+":
                numbers_stack.push(numbers_stack.pop() + numbers_stack.pop())
            if el == "*":
                numbers_stack.push(numbers_stack.pop() * numbers_stack.pop())

        if el.isdigit():
            numbers_stack.push(int(el))

        if el == '=':
            return numbers_stack.peek()


