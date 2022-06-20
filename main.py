def get_input():
    # Get input from user
    return input("Enter a word: ")


def set_list_word(word):
    # Set list of word
    list_word = list(word)
    return list_word

def ascii_list(list_word):

    list_ascii = []
    for i in list_word:
        list_ascii.append(ord(i))
    return list_ascii

def convert_bin(list_ascii):
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


