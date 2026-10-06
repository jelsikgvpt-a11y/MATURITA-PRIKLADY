subor = open("tabulka_pocetnosti.txt")
text = subor.read()

print(text)

pocty = [0] * 26

for znak in text.upper():
    if "A" <= znak <= "Z":
        pocty[ord(znak) - ord("A")] += 1

print("Počty jednotlivých znakov v texte:")

for i in range(26):
    print(chr(i + ord("A")), "-", pocty[i])

print("Znaky, ktoré sa nevyskytli:")

for i in range(26):
    if pocty[i] == 0:
        print(chr(i + ord("A")))