from enum import Enum

def lectureDuFichier(chemin):
    f = open(chemin,"r")
    lignes = f.read()
    f.close()
    return lignes

def constructionMatrice(lignes):
    lignes = lignes.split("\n")
    matrice = []
    depart = ()
    for i,l in enumerate(lignes):
        matrice.append([])
        for c, case in enumerate(l.strip()):  
            if i == 0 and case == ".":
                depart = (c, i)
            if i == len(lignes)-1 and case == ".":
                arrivee = (c ,i)
            matrice[i].append(case)
            
    return matrice, depart, arrivee

class Direction(Enum):
    NORD = (0 , -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

dicoPente = {'^': (0 , -1), '>': (1, 0), 'v': (0, 1), '<':(-1, 0)}

matrice, depart, arrivee= constructionMatrice(lectureDuFichier("advent code 2023\\input23.txt"))

croisement = [depart, arrivee]
for y in range(len(matrice)):
    for x in range(len(matrice[0])):
        if matrice[y][x] != "#":
            nbr = 0
            for dir in Direction:
                    dx, dy = dir.value
                    x1 = x + dx
                    y1 = y + dy
                    if 0<= x1 <= len(matrice[0])-1 and 0<= y1 <= len(matrice)-1 and matrice[y1][x1] != "#":
                        nbr += 1
            if nbr > 2:
                croisement.append((x,y))

graph = {}
for croix in croisement:
    graph[croix] = {}
    avisiter = [(0, croix)]
    visites = []

    while avisiter:
        dis, coor = avisiter.pop()
        visites.append(coor)
        x , y = coor
       
        for dir in Direction:
            dx, dy = dir.value
            x1 = x + dx
            y1 = y + dy

            if (x1, y1) not in visites:
                if (x1, y1) in croisement:
                    graph[croix][(x1, y1)] = dis + 1
                else:
                    if 0<= x1 <= len(matrice[0])-1 and 0<= y1 <= len(matrice)-1 and matrice[y1][x1] != "#":
                        avisiter.append((dis+1, (x1, y1)))



taille = 0
pile = [([depart], 0)]

while pile: 
    chemin, distance = pile.pop()
    pos = chemin[-1]
    if pos == arrivee:
        taille = max(taille, distance)

    for s in graph[pos]:
        if s not in chemin:
            d = distance + graph[pos][s]
            c = list(chemin)
            c.append(s)
            pile.append((c, d))


print(taille)