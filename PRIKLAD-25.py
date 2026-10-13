
import random

tipy = input("Zadaj 6 cisel od 1 do 49: ").split()
tipy = set(map(int, tipy))

zreb = set()

while len(zreb) < 6:
    zreb.add(random.randint(1, 49))

print("Vyžrebované čísla:", zreb)

uhadnute = tipy & zreb
print("Uhadnute cisla:", uhadnute)
print("Pocet uhadnutych:", len(uhadnute))

subor = open("loteria_1.txt", "r")

pocty = [0, 0, 0, 0, 0, 0, 0]

for riadok in subor:
    cisla = set(map(int, riadok.split()))
    pocet = len(cisla & zreb)
    pocty[pocet] += 1

subor.close()

print("1 uhadnute:", pocty[1])
print("2 uhadnute:", pocty[2])
print("3 uhadnute:", pocty[3])
print("5 uhadnutych:", pocty[5])
print("6 uhadnutych:", pocty[6])
