import random

subor = open("poprehadzovany_text1_vstup.txt", "r")
text = subor.read()

slova = text.split()
vysledok = []

for slovo in slova:
    stred = list(slovo[1:-1])
    random.shuffle(stred)
    vysledok.append(slovo[0] + "".join(stred) + slovo[-1])

vysledok = " ".join(vysledok)

print(vysledok)

subor = open("poprehadzovany_text1.txt", "w")
subor.write(vysledok)
subor.close()