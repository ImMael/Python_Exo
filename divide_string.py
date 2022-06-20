# split string every 6 bits
from list_to_string import list_to_string


def divide_string(string):
    """
    Split string every 6 bits
    :param string: all binary digits
    :return res: list of strings
    """
    list_string = list(string)
    list_string_divide = []
    res = []
    for i in range(0, len(list_string), 6):
        list_string_divide.append(list_string[i:i + 6])
    for i in list_string_divide:
        res.append(list_to_string(i))
        if len(res[-1]) < 6:
            for j in range(len(res[-1]), 6):
                res[-1] = "0" + res[-1]
    return res
