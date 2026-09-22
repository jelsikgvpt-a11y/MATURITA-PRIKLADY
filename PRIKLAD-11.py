# podľa zadania: otvoríme textový súbor
subor = open('sutaz_vbehu.txt')

# vytvoríme zoznam športovcov
sportovci = []

# podľa zadania: načítame celý obsah súboru
for riadok in subor:
    udaje = riadok.strip().split()

    # uložíme čas a meno športovca
    sportovci.append((int(udaje[1]), udaje[0]))

# podľa zadania: vypíšeme počet športovcov
print('Počet zúčastnených športovcov:', len(sportovci))

# podľa zadania: nájdeme najlepšieho športovca
naj, vitaz = min(sportovci)

# podľa zadania: vypíšeme meno víťaza a jeho čas v minútach a sekundách
print('Najlepší športovec:', vitaz, 's časom',
      naj // 60, 'min.', naj % 60, 'sek.')