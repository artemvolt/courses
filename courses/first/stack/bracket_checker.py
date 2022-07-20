from tokenize import String

from courses.first.stack.Stack import Stack


def bracket_check(bracket: String):
    if len(bracket) % 2 != 0:
        return False

    stack = Stack()

    for item in bracket:
        if item == '(':
            stack.push(item)
            continue

        if stack.size() == 0:
            return False
        else:
            stack.pop()

    return True
