def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    vowels = ["A", "E", "I", "O", "U"]

    for l in range(len(string)):
        if string[l] in vowels:
            Kevin += len(string) - l
        else:
            Stuart += len(string) - l

    if Kevin > Stuart:
        print("Kevin " + str(Kevin))
    elif Kevin < Stuart:
        print("Stuart " + str(Stuart))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)