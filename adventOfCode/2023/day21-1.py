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

matrice, depart= constructionMatrice(lectureDuFichier("adventOfCode\\2023\\test.txt"))


def checkNextStep(point):
    x = point[0]
    y = point[1]
    liste = []
    if y != 0: 
        if matrice[y-1][x] != "#": liste.append((x, y-1))
    if y != len(matrice)-1 : 
        if matrice[y+1][x] != "#": liste.append((x, y+1))
    if x != 0: 
        if matrice[y][x-1] != "#": liste.append((x-1, y))
    if x != len(matrice[0])-1 :
        if matrice[y][x+1] != "#":liste.append((x+1, y))
    return liste


position = [[depart]]
for i in range(1,65,1):
    position.append([])
    for p in position[i-1]:
        nextSteps = checkNextStep(p)
        for ns in nextSteps:
            if ns not in position[i]:
                position[i].append(ns)


for i in position:
    print(len(i))