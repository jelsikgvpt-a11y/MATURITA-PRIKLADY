
subor = open("spokojnost_1.txt", encoding="utf-8")

hodiny = [0] * 24
pocet_dni = [0]
celkom = 0
den = 0
predchadzajuci = ""

for riadok in subor:
    cas, odpoved = riadok.strip().split()
    hodina = int(cas.split(":")[0])

    if predchadzajuci != "" and cas < predchadzajuci:
        den += 1
        pocet_dni.append(0)

    pocet_dni[den] += 1
    hodiny[hodina] += 1
    celkom += 1

    predchadzajuci = cas

subor.close()

print("Počet všetkých vyjadrení:", celkom)

for h in range(24):
    if hodiny[h] > 0:
        print("Hodina:", h, "Reakcií zákazníkov:", hodiny[h])

print("Počet dní:", den + 1)

for i in range(den + 1):
    print(i + 1, ". deň - počet reakcií:", pocet_dni[i])
