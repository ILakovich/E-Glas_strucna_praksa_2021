print("Unesite broj stanica: ")
brojStanica = abs(int(input()))
print("\n")

putniciIzlaz = None
putniciUlaz = None
trenutnoStanje = 0
stanice = []


for x in range(1, brojStanica):
    if(x==1):
        print("Unesite broj putnika koji su usli tramvaj na " + str(x) + ". stanici: ")
        putniciUlaz = abs(int(input()))
        trenutnoStanje += putniciUlaz
        stanice.append(trenutnoStanje)
        print("\n")

        print(trenutnoStanje)
        print(stanice)

    else:
        print("Unesite broj putnika koji su izašli iz tramvaja na " + str(x) + ". stanici: ")
        putniciIzlazSave = putniciIzlaz
        putniciIzlaz = abs(int(input()))

        if(putniciIzlaz > trenutnoStanje):
            while(putniciIzlaz > trenutnoStanje):
                print("Broj putnika koji su izašli ne može biti veći od broja putnika koji su ušli, unesite ponovo")
                putniciIzlaz = abs(int(input()))

        trenutnoStanje -= putniciIzlaz
        print(trenutnoStanje)
        print(stanice)
        print("Unesite broj putnika koji su usli u tramvaj na " + str(x) + ". stanici: ")
        putniciUlaz = abs(int(input()))
        trenutnoStanje += putniciUlaz
        print(trenutnoStanje)
        stanice.append(trenutnoStanje)
        print("\n")
        print(trenutnoStanje)
        print(stanice)

trenutnoStanje = 0
stanice.append(0)
max = max(stanice)
print(stanice)
print("\n")
print("Na zadnoj (" + str(x+1) + ") stanici, svi su putnici izašli.")
print("Minimalni potrebni kapacitet tramvaja je " + str(max) + " mjesta.")