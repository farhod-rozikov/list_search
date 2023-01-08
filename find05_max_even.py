def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    data.sort()
    i = 0
    while i < len(data):
        if data[i] % 2 == 0:
            return data[i]            
        i += 1