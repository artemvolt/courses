from tokenize import String

from courses.first.deque.Deque import Deque


def check_palidrom(input_raw: String):
    deque = Deque()
    for i in input_raw:
        deque.addTail(i)

    if deque.size() <= 2:
        return False

    while deque.size() >= 2:
        if not deque.removeFront() == deque.removeTail():
            return False

    return True
