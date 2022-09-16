import variables as v


def run():
    v.userInput = input("Adjon meg egy mondatot: \n")
    count(v.userInput)
    reverse(v.userInput)
    makeList(v.userInput)


def count(txt):
    for x in txt:
        if x in v.letters:
            v.letters[x] += 1
        else:
            v.letters[x] = 1
    print("Betűk gyakorisága: ", v.letters)


def reverse(txt):
    print(txt[::-1])


def makeList(txt):
    v.listOfWords = txt.split(' ')
    print("Listába rendezve szavanként: ", v.listOfWords)


if __name__ == '__main__':
    run()
