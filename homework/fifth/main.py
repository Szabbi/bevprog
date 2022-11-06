import string


def fel1():
    sortLine = "{0:>10}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}"
    sortColumn = "{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}"

    print(sortLine.format("1", "2", "3", "4", "5",
          "6", "7", "8", "9", "10", "11", "12", end=''))

    print("    :------------------------------------------------------------")

    sortColumn = "{0:>5}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}"
    for i in range(1, 13):
        print(sortColumn.format(str(i) + ":", i*1, i*2, i*3, i*4, i*5, i*6,
                                i*7, i*8, i*9, i*10, i*11, i*12, end=''))


def fel2(txt):
    return a(txt) == a(txt)[::-1]


def a(txt):
    stripped = ""
    for x in txt:
        if x not in string.punctuation:
            stripped += x.lower()
    return stripped.replace(" ", "")


if __name__ == '__main__':
    fel1()
    inputtxt = input("Text: ")
    if fel2(inputtxt):
        print(f"{a(inputtxt)} is a palindrome!")
