def run():
    inputNum = input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n")
    v.inputUnit = input()
    print(convert(inputNum, v.inputUnit), "inches")


def convert(num, unit):
    match unit:
        case "cm":
            return float(num) * v.convNum
        case "inch":
            return float(num) / v.convNum
        case _:
            return "Isn't a correct unit!"


class v:
    convNum = 2.54
    userInputUnit = ""
    inputUnit = ""


if __name__ == '__main__':
    run()
