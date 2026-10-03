import random

def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

subor = open("poprehadzovany_text_vstup2.txt", "r")
text = subor.read()

slova = text.split()
vysledok = []

for slovo in slova:
    zaciatok = 0
    koniec = len(slovo)

    while zaciatok < koniec and not slovo[zaciatok].isalpha():
        zaciatok += 1

    while koniec > zaciatok and not slovo[koniec - 1].isalpha():
        koniec -= 1

    if koniec - zaciatok > 2:
        nove = slovo[zaciatok] + pomiesaj(slovo[zaciatok + 1:koniec - 1]) + slovo[koniec - 1]
        slovo = slovo[:zaciatok] + nove + slovo[koniec:]

    vysledok.append(slovo)

vysledok = " ".join(vysledok)

print(vysledok)

subor = open("poprehadzovany_text.txt", "w")
subor.write(vysledok)
subor.close()