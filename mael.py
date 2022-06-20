def get_input():
    # Get input from user
    return input("Enter a word: ")


while True:
    # Main loop
    text = get_input()
    if text != "":
        print(text)
