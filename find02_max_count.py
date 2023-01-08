def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i, _max = 1, 1
    data.sort(reverse=True)
    while i < len(data):
        if data[i] == data[0]:
            _max += 1
        i += 1
    return _max
