import re

f = open("test.txt","r")
lignes = f.readlines()
f.close()

def calculerPlusCourtChemin(p, p2):
    distance = abs(p[0]-p2[0]) + abs(p[1]-p2[1])

    return distance

# RECUPERATION DE L INPUT
galaxie = []
for y in lignes:
    galaxie.append(y.strip())

# RECHERCHE DES LIGNES OU IL N Y A PAS DE GALAXIE
ligneAAdd = []
for y in range(len(galaxie)):
    if not("#" in galaxie[y]):
        ligneAAdd.append(y)

for l in ligneAAdd:
    galaxie.insert(l + ligneAAdd.index(l), "."*len(galaxie[0]))

# RECHERCHE DES COLONNES OU IL N Y A PAS DE GALAXIE 
colonneAAdd = []
for x in range(len(galaxie[0])):
    gala = False
    for y, ligne in enumerate(galaxie):
        if "#" == galaxie[y][x]:
            gala = True
    if not(gala):
        colonneAAdd.append(x)

for x in colonneAAdd:
    for y, ligne in enumerate(galaxie):
        galaxie[y] = galaxie[y][:x+colonneAAdd.index(x)+1] + "." + galaxie[y][x+colonneAAdd.index(x) + 1:]

#RECUPERATION DES GALAXIES
planete = []
for x in range(len(galaxie[0])):
    gala = False
    for y, ligne in enumerate(galaxie):
        if "#" == galaxie[y][x]:
            planete.append((x,y))
# CALCULE PLUS COURT CHEMIN ENTRE CHAQUE PAIR
sommeChemin = 0

for i, p in enumerate(planete):
    for y, p2 in enumerate(planete[i+1:], i+1):
        distance = calculerPlusCourtChemin(p, p2)
        sommeChemin += distance

print(sommeChemin)

