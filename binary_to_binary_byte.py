# add 0 to transform binary to binary byte
def add_0_to_start_wordlist(wordlist):
    res = []
    for word in wordlist:
        if len(word) < 8:
            word = "0" + word
            res.append(word)
    return res

