from heapq import heappush, heappop
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

matrice, depart, arrivee= constructionMatrice(lectureDuFichier("advent code 2023\\test.txt"))


def faireChemin(matrice, depart, arrivee):
    taille = 0
    pile = [(depart, [depart])]

    while pile: 
        pos, chemin = pile.pop()

        if pos == arrivee:
            taille = max(taille, len(chemin) -1)

        x,y = pos

        suivant = []

        if matrice[y][x] in dicoPente:
            dx, dy = dicoPente[matrice[y][x]]
            x1 = x + dx
            y1 = y + dy
            if 0<= x1 <= len(matrice[0])-1 and 0<= y1 <= len(matrice)-1:
                if matrice[y1][x1] != "#" and (x1, y1) not in chemin:
                    suivant.append((x1, y1))
        else:
            for dir in Direction:
                    dx, dy = dir.value
                    x1 = x + dx
                    y1 = y + dy
                    if 0<= x1 <= len(matrice[0])-1 and 0<= y1 <= len(matrice)-1:
                        if matrice[y1][x1] != "#" and (x1, y1) not in chemin:
                            suivant.append((x1, y1))
        for s in suivant:
            c = list(chemin)
            c.append(s)
            pile.append((s, c))
    
    return taille

resultat = faireChemin(matrice, depart, arrivee)

# Exercice 1: 2278 
print('Exercice 1:', resultat)

    


    