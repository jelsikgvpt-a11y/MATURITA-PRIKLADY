def spracuj_riadok(riadok):
    vysledok = []
    pocet = 0
    znak = "0"

    for i in riadok:
        if i == znak:
            pocet += 1
        else:
            vysledok.append(str(pocet))
            pocet = 1
            znak = i

    vysledok.append(str(pocet))

    return " ".join(vysledok)


subor = open("kompresia_obrazka_1.txt", "r")
rozmery = subor.readline().split()

sirka = int(rozmery[0])
vyska = int(rozmery[1])

print("Sirka:", sirka)
print("Vyska:", vyska)
print("Pocet bodov:", sirka * vyska)

vystup = open("kompresia_obrazka_vystup.txt", "w")
vystup.write(str(sirka) + " " + str(vyska) + "\n")

for i in range(vyska):
    riadok = subor.readline().strip()
    vysledok = spracuj_riadok(riadok)
    vystup.write(vysledok + "\n")

subor.close()
vystup.close()