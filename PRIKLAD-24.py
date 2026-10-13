
import random

volba = input("Chces sifrovat alebo desifrovat? (s/d): ")

if volba == "s":
    vstup = open("vstupny_text.txt", "r", encoding="utf-8")
    vystup = open("zasifrovany_text_2.txt", "w", encoding="utf-8")

    for riadok in vstup:
        posun = random.randint(1, 25)
        novy = ""

        for znak in riadok:
            if znak >= "a" and znak <= "z":
                novy += chr((ord(znak) - ord("a") + posun) % 26 + ord("a"))
            else:
                novy += znak

        pismeno = chr(ord("a") + posun)
        vystup.write(pismeno + novy)

    vstup.close()
    vystup.close()

elif volba == "d":
    vstup = open("zasifrovany_text_2.txt", "r", encoding="utf-8")
    vystup = open("desifrovany_text.txt", "w", encoding="utf-8")

    for riadok in vstup:
        posun = ord(riadok[0]) - ord("a")
        novy = ""

        for znak in riadok[1:]:
            if znak >= "a" and znak <= "z":
                novy += chr((ord(znak) - ord("a") - posun) % 26 + ord("a"))
            else:
                novy += znak

        vystup.write(novy)

    vstup.close()
    vystup.close()
