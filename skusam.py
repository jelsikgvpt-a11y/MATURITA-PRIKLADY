import random

tipy = input("Zadaj 6 cisel od 1 do 49: ").split()
tipy = set(map(int,tipy))

zreb = set()
while len(zreb) < 6:
    zreb.add(random.randint(1, 49))

print("vyzrebovane cisla:" , "zreb")

uhadnute = tipy & zreb
print("uhadnute cisla:", uhadnute)
print("pocet uhadnutyvh:", len(uhadnute))

subor = open("loteria_1.txt", "r")

pocty = [0,0,0,0,0,0,0]

for riadok in subor:
    cisla = set(map(int, riadok.split()))
    pocet = len(cisla & zreb)
    pocty[pocet] += 1

subor.close()