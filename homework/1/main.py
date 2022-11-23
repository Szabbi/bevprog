def run():
    inputText = input("Adjon meg egy mondatot:\n")
    count(inputText)
    reverse(inputText)
    list(inputText)


def count(text):
    for x in text:
        if x in v.letters:
            v.letters[x] += 1
        else:
            v.letters[x] = 1
    print(f"Betűk gyakorisága: {v.letters}")


def reverse(text):
    print(f"Fordítva: {text[::-1]}")


def list(text):
    v.listOfWords = text.split(' ')
    print(f"Listába rendezve szavanként: {v.listOfWords}")


class v:
    letters = {}
    listOfWords = []


if __name__ == '__main__':
    run()
