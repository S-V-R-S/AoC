from enum import Enum

def lectureDuFichier(chemin):
    f = open(chemin,"r")
    lignes = f.read()
    f.close()
    return lignes

def constructionMatrice(lignes):
    depart = ()
    lignes = lignes.split("\n")
    matrice = []
    for i,l in enumerate(lignes):
        matrice.append([])
        for c, case in enumerate(l.strip()):
            if case =="S": depart = (c, i)
            matrice[i].append(case)
    return matrice, depart

# matrice, depart= constructionMatrice(lectureDuFichier("adventOfCode\\2023\\test.txt"))

matrice, depart= constructionMatrice(lectureDuFichier("adventOfCode\\2023\\input21.txt"))

class Direction(Enum):
    NORD = (0 , -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

def positionPossible(depart, nbrPas):
    visites = {depart}
    pile = [(depart, nbrPas)]
    pixel = set()

    while pile:
        point, dis = pile[0]
        del pile[0]

        # pour gagner du temps, comme on peut revenir en arriere qd le nbr de pas restants est pairs c'est comme sil restait 0 
        if dis % 2 == 0:
            pixel.add(point)
        if dis == 0:
            continue
        
        x,y= point
        for dir in Direction:
            dx, dy = dir.value
            x1 = x + dx
            y1 = y + dy

            if 0<= x1 <= len(matrice[0])-1 and 0<= y1 <= len(matrice)-1 and matrice[y1][x1] != "#" and (x1,y1) not in visites:
                    pile.append(((x1, y1), dis - 1))
                    visites.add((x1,y1))
    return len(pixel)

nbrDePas = 26501365

# c un carre 
taille = len(matrice)
# nbr de cubes entier si on va tout droit
nbrGrille = nbrDePas // taille - 1

# les diagonales 
nbrImpairs = nbrGrille**2

# les diagonales
nbrPairs = (nbrGrille+1)**2

# car le nbr de depart est impairs
pairs = positionPossible(depart, 2000)

# car le nbr de depart est impairs
impairs = positionPossible(depart, 2001)


# les quatres du sommet 
top = positionPossible((taille//2, len(matrice)-1), taille-1)
bot = positionPossible((taille//2, 0), taille-1)
left = positionPossible((len(matrice)-1, taille//2), taille-1)
right = positionPossible((0, taille//2), taille-1)


# il y a deux autres types de carres non pleins 

# les plus petits
# on commence tjrs a un angle
# taille//2 - 1: -1 car on est deja sur une case au depart de la fct et taille//2 car c le nbr de pas quil nous reste 
ptr = positionPossible((0, taille-1), taille//2-1)
ptl = positionPossible((taille-1, taille-1), taille//2-1)
pbr = positionPossible((0, 0), taille//2-1)
pbl = positionPossible((taille-1, 0), taille//2-1)

# les plus gros 
# nbrDePas - nbrGrille*taille-1 : -1 car on est deja sur une case au depart de la fct, nbrDePas - nbrGrille*taille c'est le nbr de pas qui reste 
gtr = positionPossible((0, taille-1), nbrDePas - nbrGrille*taille-1)
gtl = positionPossible((taille-1, taille-1), nbrDePas - nbrGrille*taille-1)
gbr = positionPossible((0, 0), nbrDePas - nbrGrille*taille-1)
gbl = positionPossible((taille-1, 0), nbrDePas - nbrGrille*taille-1)

somme = top + bot + left + right + pairs*nbrPairs + impairs*nbrImpairs + (nbrGrille+1)*(ptr+ptl+pbr+pbl) + nbrGrille*(gtr+gtl+gbr+gbl)
print(somme)

print(629720570456311==somme)




