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

# matrice, depart= constructionMatrice(lectureDuFichier("advent code 2023\\test.txt"))

matrice, depart= constructionMatrice(lectureDuFichier("advent code 2023\\input21.txt"))

class Direction(Enum):
    NORD = (0 , -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

def positionPossible(x , y, nbrPas):
    depart = (x,y)
    visites = {depart}
    pile = [(depart, nbrPas)]
    pixel = set()

    while pile:
        point, dis = pile[0]
        del pile[0]

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


print(positionPossible(depart[0], depart[1], 64))