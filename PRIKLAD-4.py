subor = open("meteo_stanice.txt", "r", encoding="utf-8")

pocet = 0
zoz = []
teploty = []
ibateploty = []

for r in subor:
    info = r.strip()
    udaje = info.split()
    teplota = udaje[3]
    teplota = float(teplota.replace(',', '.').replace('–', '-'))
    teploty.append((teplota, info[:3])) # {riadok B}
    ibateploty.append(teplota)
    print(teplota)
    pocet += 1
    zoz.append(info)
subor.close()

print('Počet meraní:', pocet)
print('Maximum bolo v stanici:', max(teploty)[1])
priemer = sum(ibateploty)/len(teploty)
print('Priemerná teplota bola: {:5.2f} stupňov'.format(priemer))