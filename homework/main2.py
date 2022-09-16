import variables as v

def run():
    v.userInputNum = input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n")
    v.userInputUnit = input()
    convert(v.userInputNum, v.userInputUnit)


def convert(num, unit):
    if num.isnumeric() and "cm" in unit or "inch" in unit:
        if "cm" in unit:
            print(float(num) * v.convNum, "inches")
        else:
            print(float(num) / v.convNum, "cm")
    else:
        print("Isn't a number and/or not correct unit")


if __name__ == '__main__':
    run()
