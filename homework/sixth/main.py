import string
import sys
if __name__ == '__main__':
    with open('hazi', 'r', encoding="UTF-8") as txt:
        content = txt.readlines()

    vowelsList = ['a', 'e', 'i', 'o', 'u', 'á',
                  'é', 'í', 'ú', 'ó', 'ö', 'ő', 'ü', 'ű']

    def b(txt):
        stripped = []
        # repeat for each line in input
        for x in range(len(txt)):
            # remove punctuation
            for y in string.punctuation:
                txt[x] = txt[x].replace(y, "")
            # remove vowels upper- and lowercase
            for z in vowelsList:
                txt[x] = txt[x].replace(z, "")
                txt[x] = txt[x].replace(z.upper(), "")
            # append not empty lines to list
            if not txt[x].isspace():
                stripped.append(txt[x])
        return stripped

    with open('output.txt', 'w') as out:
        # repeat for list lenght and output if line index divisible by 3
        for i in range(len(b(content))):
            if i % 3 == 0:
                out.write(b(content)[i])
# remove mgh, empty line, punct., output every 3rd line
