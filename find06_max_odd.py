def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd_data = []
    i = 0
    while i < len(data):
        if data[i] % 2 == 1:
            odd_data.append(data[i])          
        i += 1
    if odd_data:
        odd_data.sort(reverse=True)
        return odd_data[0]
    else:
        return -1