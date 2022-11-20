import os
import string
if __name__ == '__main__':
    # with open('/home/szabbi/Documents/Github/bevprog/homework/sixth/hazi.txt', 'r') as txt:
    #    content = txt.readline()
    # while content:
    #    content = txt.readline()

    vowelsList = ['a', 'e', 'i', 'o', 'u', 'á',
                  'é', 'í', 'ú', 'ó', 'ö', 'ő', 'ü', 'ű']
    content = "asdaqqéáeégéásdf;;..\n\na,,q"

    def a(txt):
        stripped = ""
        for x in txt:
            if x not in string.punctuation:
                stripped += x.lower()
        return stripped

    def vowels(txt):
        noVowels = ""
        for x in txt:
            if x not in vowelsList:
                noVowels += x.lower()
        return noVowels

    stripOne = a(content)
    stripTwo = vowels(stripOne)

    with open('/home/szabbi/Documents/Github/bevprog/homework/sixth/hazi.txt', 'w') as
    print(stripTwo)
