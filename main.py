from binary_to_binary_byte import binary_to_binary_byte
from divide_string import divide_string
from list_to_string import list_to_string


def get_input():
    """
    Get input from user
    """
    return input("Enter a word: ")


def set_list_word(word):
    """
    Set list of word
    """
    list_word = list(word)
    return list_word

def ascii_list(list_word):
    """
    Convert list_word to list_ascii
    """
    list_ascii = []
    for i in list_word:
        list_ascii.append(ord(i))
    return list_ascii

def convert_bin(list_ascii):
    """
    Convert list_ascii to binary
    """
    list_bin = []
    for i in list_ascii:
        list_bin.append(bin(i).replace("0b",""))
    return list_bin




while True:
    # Main loop
    text = get_input()
    if text != "":
        list_word = set_list_word(text)
        print(list_word)
        list_ascii = ascii_list(text)
        print(list_ascii)
        list_bin = convert_bin(list_ascii)
        print(list_bin)
        list_bin_byte = binary_to_binary_byte(list_bin)
        print(list_bin_byte)
        list_bin_byte_string = list_to_string(list_bin_byte)
        print(list_bin_byte_string)
        string_divide = divide_string(list_bin_byte_string)
        print(string_divide)


