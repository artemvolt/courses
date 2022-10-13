
def sum_of_the_numbers_of_number(number: int) -> int:
    """Сумма чисел числа"""
    to_string = str(number)
    length_string = len(to_string)
    if length_string == 1:
        return number

    first_number = int(to_string[:1])
    others = int(to_string[1:])
    return first_number + sum_of_the_numbers_of_number(others)
