def GenerateBBSTArray(_input: list) -> list:
    if len(_input) == 0:
        return []

    sorted_input = sorted(_input)
    result = [None] * len(_input)
    return GenerateBBSTArrayRecursive(result, sorted_input, 0)


def GenerateBBSTArrayRecursive(result: list, sorted_input: list, index: int) -> list:
    middle_index = len(sorted_input) // 2
    result[index] = sorted_input[middle_index]
    left_subtree = sorted_input[:middle_index]
    if len(left_subtree) > 0:
        GenerateBBSTArrayRecursive(result, left_subtree, 2 * index + 1)

    right_subtree = sorted_input[middle_index + 1:]
    if len(right_subtree) > 0:
        GenerateBBSTArrayRecursive(result, right_subtree, 2 * index + 2)

    return result
