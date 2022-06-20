def binary_to_binary_byte(wordlist):
    """
    Converts a list of binary words to a list of binary bytes.
    :param wordlist:
    :return res:
    """
    res = []
    for word in wordlist:
        if len(word) < 8:
            word = "0" + word
            res.append(word)
    return res

