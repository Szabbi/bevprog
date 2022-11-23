class Team:
    devNevList = []
    devProjectList = []

    def __init__(self, nev, project, role):
        self.devNevList.append(nev)
        self.devProjectList.append(project)
        self.nev = nev
        self.project = project
        self.role = role


def main():
    dev1 = Team("Peti", "SolArch", "Frontend")
    print("-- Developer létrehozva. --")
    print(f"{dev1.nev} a {dev1.project}-en dolgozik {dev1.role} szerepkörben.")

    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    print("-- Developer létrehozva. --")
    print(f"{dev2.nev} a {dev2.project}-en dolgozik {dev2.role} szerepkörben.")

    dev3 = Team("Peti", "KefERP", "Backend")
    print("-- Developer létrehozva. --")
    print(f"{dev3.nev} a {dev3.project}-en dolgozik {dev3.role} szerepkörben.")

    dev4 = Team("Éva", "KefERP", "Frontend")
    print("-- Developer létrehozva. --")
    print(f"{dev4.nev} a {dev4.project}-en dolgozik {dev4.role} szerepkörben.")

    if (dev1.project == dev2.project):
        print(f"{dev1.nev} és {dev2.nev} dolgoznak egy projekten")
    elif (dev1.project == dev3.project):
        print(f"{dev1.nev} és {dev3.nev} dolgoznak egy projekten")
    elif (dev1.project == dev4.project):
        print(f"{dev1.nev} és {dev3.nev} dolgoznak egy projekten")
    elif (dev2.project == dev3.project):
        print(f"{dev2.nev} és {dev3.nev} dolgoznak egy projekten")
    elif (dev2.project == dev4.project):
        print(f"{dev2.nev} és {dev3.nev} dolgoznak egy projekten")
    else:
        print(f"{dev3.nev} és {dev4.nev} dolgoznak egy projekten")


if __name__ == '__main__':
    main()
