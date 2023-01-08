def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i, _m_odd = 0, 0
    while i < data[i]:
        if _m_odd < data[i] and data[i] % 2 == 1:
            _m_odd = data[i]
        i += 1
    return _m_odd