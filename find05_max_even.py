from audioop import reverse
from pip import main


def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even_data = []
    i = 0
    while i < len(data):
        if data[i] % 2 == 0:
            even_data.append(data[i])          
        i += 1
    if even_data:
        even_data.sort(reverse=True)
        return even_data[0]
    else:
        return -1
    
print(find_max_even([1,3,7,9,5]))