klic = input("Kluc: ")
volba = input("Sifrovat alebo desifrovat? ")

vstup = open("vstupny_text.txt", "r")
vystup = open("vystup.txt", "w")

for riadok in vstup:
    vysledok = ""
    i = 0

    for znak in riadok:
        if "a" <= znak <= "z":
            posun = ord(klic[i % len(klic)]) - ord("a") + 1

            if volba == "desifrovat":
                posun = -posun

            znak = chr((ord(znak) - ord("a") + posun) % 26 + ord("a"))
            i += 1

        vysledok += znak

    vystup.write(vysledok)

vstup.close()
vystup.close()