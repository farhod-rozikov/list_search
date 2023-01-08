def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i, _m_even = 0, 0
    while i < data[i]:
        if _m_even > data[i] and data[i] % 2 == 0:
            _m_even = data[i]
        i += 1
    return _m_even