subor = open("skok_do_dialky.txt", encoding="utf-8")

krajiny = []
pocet = []
vitazi = []
najlepsi = 0

for riadok in subor:
    udaje = riadok.split()

    meno = udaje[0]
    krajina = udaje[1]

    if krajina not in krajiny:
        krajiny.append(krajina)
        pocet.append(1)
    else:
        cislo = krajiny.index(krajina)
        pocet[cislo] += 1

    maximum = max(int(udaje[2]), int(udaje[3]), int(udaje[4]), int(udaje[5]), int(udaje[6]))
    if maximum > najlepsi:
        najlepsi = maximum
        vitazi = [meno]
    elif maximum == najlepsi:
        vitazi.append(meno)

print("Krajiny:", krajiny)
for i in range(len(krajiny)):
    print(krajiny[i], pocet[i])

print("Vitazi:", vitazi)

