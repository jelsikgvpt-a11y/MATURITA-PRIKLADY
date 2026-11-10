def spracuj_riadok(riadok):
    cisla = riadok.split()
    text = ""
    farba = "0"
    for c in cisla:
        text += farba * int(c)
        if farba == "0":
            farba = "1"
        else:
            farba = "0"
    return text


vstup = open("dekompresia_obrazka_1.txt")
rozmery = vstup.readline().strip()
sirka, vyska = rozmery.split()
print("Šírka:", sirka, "Výška:", vyska, "Počet bodov:", int(sirka) * int(vyska))

prvy_riadok = vstup.readline().strip()
print(spracuj_riadok(prvy_riadok))

vystup = open("dekompresia_obrazka_vystup.txt", "w")
vystup.write(rozmery + "\n")
vystup.write(spracuj_riadok(prvy_riadok) + "\n")
for riadok in vstup:
    vystup.write(spracuj_riadok(riadok.strip()) + "\n")

vstup.close()
vystup.close()