def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    even_data = []
    i = 0
    while i < len(data):
        if data[i] % 2 == 0:
            even_data.append(data[i])          
        i += 1
    if even_data:
        even_data.sort()
        return even_data[0]
    else:
        return -1