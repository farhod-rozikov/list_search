def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i, _min = 0, data[0]
    while i < len(data):
        if _min > data[i]:
            _min = data[i]
        i += 1
    return data.index(_min)