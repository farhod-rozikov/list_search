from find02_max_count import find_max_count


def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    i, _max = 0, 0
    while i < len(data):
        if _max < data[i]:
            _max = data[i]
        i += 1
    return data.index(_max)