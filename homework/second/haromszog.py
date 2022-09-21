def run():
    print("Adja meg a háromszög három oldalát cm-ben:")
    inputA = float(input("a oldal (cm): "))
    inputB = float(input("b oldal (cm): "))
    inputC = float(input("c oldal (cm): "))
    calc(inputA, inputB, inputC)


def calc(sideA, sideB, sideC):
    l = [sideA, sideB, sideC]
    l.sort()
    if l[0] + l[1] >= l[2]:
        print(f"A(z) {sideA}, {sideB} és {sideC} oldalú háromszög megszerkeszthető.")
    else:
        print(f"A(z) {sideA}, {sideB} és {sideC} oldalú háromszög NEM megszerkeszthető.")


if __name__ == '__main__':
    run()
