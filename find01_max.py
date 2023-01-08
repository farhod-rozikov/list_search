from audioop import reverse


def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    data.sort(reverse=True)
    return data[0]
    