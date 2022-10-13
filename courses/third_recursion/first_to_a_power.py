
def number_to_a_power(number: int, power: int) -> int:
    """Возведение числа в степень"""
    if power == 0:
        return 1

    return number * number_to_a_power(number, power - 1)
