def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i, _min = 1, 1
    data.sort()
    while i < len(data):
        if data[i] == data[0]:
            _min += 1
        i += 1
    return _min
