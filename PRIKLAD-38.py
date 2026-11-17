
subor = open("spokojnost_1.txt", encoding="utf-8")

spokojni = [0] * 24
nespokojni = [0] * 24
celkom = 0

for riadok in subor:
    cas, odpoved = riadok.strip().split()
    hodina = int(cas.split(":")[0])

    celkom += 1

    if odpoved == "áno":
        spokojni[hodina] += 1
    else:
        nespokojni[hodina] += 1

subor.close()

print("Celkový počet vyjadrení:", celkom)

print("Najviac spokojných:", max(spokojni), "počas hodiny", spokojni.index(max(spokojni)))

print("Najviac nespokojných:", max(nespokojni), "počas hodiny", nespokojni.index(max(nespokojni)))

for h in range(24):
    spolu = spokojni[h] + nespokojni[h]

    if spolu > 0:
        percenta = spokojni[h] / spolu * 100
        print(h, "hodina:", round(percenta, 2), "%")
