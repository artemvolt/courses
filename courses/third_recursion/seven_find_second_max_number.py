def find_second_max_number(items: list):
    """Поиск второго максимального числа"""
    if len(items) <= 1:
        return None

    first_max = items[0]
    second_max = items[1]
    if first_max < second_max:
        first_max = items[1]
        second_max = items[0]

    return compare_current_with_max_and_second(items[2:], first_max, second_max)


def compare_current_with_max_and_second(items: list, first_max: int, second_max: int) -> int:
    if len(items) == 0:
        return second_max

    current = items[0]

    if second_max < current <= first_max:
        second_max = current

    if current > first_max:
        second_max = first_max
        first_max = current

    return compare_current_with_max_and_second(items[1:], first_max, second_max)
