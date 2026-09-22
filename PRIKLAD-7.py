import random

# podľa zadania: zadáme počet študentov a počet otázok
pocet_studentov = int(input('Zadaj počet študentov: '))
pocet_otazok = int(input('Zadaj počet otázok: '))

# podľa zadania: počet otázok nesmie byť menší ako počet študentov
while pocet_otazok < pocet_studentov:
    print('Chyba: počet otázok nemôže byť menší ako počet študentov!')
    pocet_otazok = int(input('Zadaj počet otázok: '))

# podľa zadania: vytvoríme čísla študentov 1 až počet študentov
studenti = []
for i in range(pocet_studentov):
    studenti.append(i + 1)

# podľa zadania: vytvoríme čísla otázok 1 až počet otázok
otazky = []
for i in range(pocet_otazok):
    otazky.append(i + 1)

# podľa zadania: párne a nepárne otázky sa musia striedať
parne_otazky = otazky[1::2]
neparne_otazky = otazky[::2]

random.shuffle(parne_otazky)
random.shuffle(neparne_otazky)

otazky = []

for i in range(len(parne_otazky)):
    otazky = otazky + [parne_otazky[i], neparne_otazky[i]]

# ak je nepárnych otázok viac, pridáme poslednú
if len(neparne_otazky) > len(parne_otazky):
    otazky.append(neparne_otazky[-1])

# podľa zadania: študenti pôjdu odpovedať v náhodnom poradí
random.shuffle(studenti)

# podľa zadania: ak nechceme striedanie párnych a nepárnych otázok,
# stačí odkomentovať tento riadok
# random.shuffle(otazky)

# podľa zadania: vypíšeme poradie študentov a ich otázky
print('Poradie odpovedajúcich a ich číslo otázky:')

for i in range(pocet_studentov):
    print('{}. študent: {}, otázka: {}'.format(i + 1, studenti[i], otazky[i]))