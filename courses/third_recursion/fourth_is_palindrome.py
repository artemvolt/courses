from tokenize import String


def is_palindrome(_input: String) -> bool:
    """Является ли строка палиндромом"""
    if len(_input) < 2:
        return False

    first = _input[0]
    last = _input[-1]
    catted = _input[1:-1]

    if len(catted) > 2 and first == last:
        return is_palindrome(catted)

    return first == last
