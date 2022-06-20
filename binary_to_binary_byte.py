# add 0 to transform binary to binary byte
def binary_to_binary_byte(wordlist):
    res = []
    for word in wordlist:
        if len(word) < 8:
            word = "0" + word
            res.append(word)
    return res

