# podľa zadania: otvoríme textový súbor
subor = open('bus_vytazenost.txt')

# podľa zadania: načítame kapacitu autobusu z prvého riadku
kapacita = int(subor.readline())

# zoznam všetkých zastávok
zoznam = []

# zoznam zastávok, po ktorých bol autobus preplnený
pretazene = []

# aktuálny počet ľudí v autobuse
pocet = 0

# najväčšie preťaženie
naj = 0

# podľa zadania: spracujeme všetky zastávky
for riadok in subor:
    udaje = riadok.split()

    # podľa zadania: názov zastávky môže byť jedno- alebo dvojslovný
    if len(udaje) == 3:
        nazov = udaje[2]
    else:
        nazov = udaje[2] + ' ' + udaje[3]

    # počet ľudí = nastúpia - vystúpia
    pocet += int(udaje[0])
    pocet -= int(udaje[1])

    # podľa zadania: zistíme, či je autobus preplnený
    if pocet > kapacita:
        pretazene.append(nazov)

        # podľa zadania: zistíme najväčšie preťaženie
        if pocet - kapacita > naj:
            naj = pocet - kapacita

    # pridáme zastávku do zoznamu
    zoznam.append(nazov)

# podľa zadania: vypíšeme počet zastávok
print('Počet zastávok:', len(zoznam))

# podľa zadania: vypíšeme všetky zastávky v jednom riadku
print('Zastávky na trase: ', end='')

for zastavka in zoznam:
    print(zastavka, end=', ')

print()

# podľa zadania: vypíšeme zastávky, kde bol autobus preplnený
print('Autobus bol preplnený po vyjdení zo zastávok:')

for zastavka in pretazene:
    print(zastavka)

# podľa zadania: vypíšeme najväčšie preťaženie
print('Najväčšie preťaženie o', naj, 'ľudí.')