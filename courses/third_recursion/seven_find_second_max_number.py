def find_second_max_number(items: list):
    """Поиск второго максимального числа"""
    if len(items) == 0:
        return None

    current = items[0]
    first_max = second_max = current

    return compare_current_with_max_and_second(items[1:], first_max, second_max)


def compare_current_with_max_and_second(items: list, first_max: int, second_max: int) -> int:
    if len(items) == 0:
        return second_max

    current = items[0]

    if current == first_max:
        second_max = current

    if current > first_max:
        second_max = first_max
        first_max = current

    if second_max < current < first_max:
        second_max = current

    return compare_current_with_max_and_second(items[1:], first_max, second_max)
