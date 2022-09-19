def run():
    inputA = float(input("Adja meg az A oldal hosszát: "))
    inputB = float(input("Adja meg a B oldal hosszát: "))
    inputC = float(input("Adja meg a C oldal hosszát: "))
    check(inputA, inputB, inputC)


def check(sideA, sideB, sideC):
    lenghts = [sideA, sideB, sideC]
    lenghts.sort()
    if lenghts[0] + lenghts[1] >= lenghts[2]:
        print("A háromszög megrajzolható.")
    else:
        print("Nem rajzolható meg a háromszög.")


if __name__ == '__main__':
    run()
