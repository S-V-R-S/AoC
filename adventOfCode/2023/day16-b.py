
f = open("advent code 2023/input.txt","r")
lignes = f.read()
f.close()
matrice = []
matriceLumiere = []

def compter(matriceLumiere):
    nbr = 0
    for y in range(len(matriceLumiere)):
        for x in range(len(matriceLumiere[0])):
            if matriceLumiere[y][x] == "#":
                nbr += 1
    return nbr
matrice2 = []
for y, ligne in enumerate(lignes.split("\n")):
        matrice2.append([])
        for ch in ligne:
            matrice2[y].append(ch)


def explorer(ABouger):
    matriceLumiere = []
    matrice = []
    for y, ligne in enumerate(lignes.split("\n")):
        matrice.append([])
        matriceLumiere.append([])
        for ch in ligne:
            matrice[y].append(ch)
            matriceLumiere[y].append('')
    matriceLumiere[ABouger[0][0][1]][ABouger[0][0][0]] = "#"

    direction = {"|": {(0,1):[(0,1)], (0,-1):[(0,-1)], (1,0):[(0,-1),(0,1)], (-1,0):[(0,-1),(0,1)]},
                "-": {(1,0):[(1,0)], (-1,0):[(-1,0)], (0,1):[(1,0),(-1,0)], (0,-1):[(1,0),(-1,0)]},
                "/": {(1,0):[(0,-1)], (-1,0):[(0,1)], (0,1):[(-1,0)], (0,-1):[(1,0)]},
                "\\": {(1,0):[(0,1)], (-1,0):[(0,-1)], (0,1):[(1,0)], (0,-1):[(-1,0)]}}

    dicoDejaFait = {str(ABouger[0]):1}

    while(len(ABouger)!=0):
        newABouger = []
        for p, point in enumerate(ABouger):
            pt = point[0]
            vecteur = point[1]
            pos = matrice[pt[1]][pt[0]]
            if pos not in direction:
                x = pt[0]+vecteur[0]
                y = pt[1]+vecteur[1]
                newPos = (x,y)
                if(-1 not in newPos and x != len(matriceLumiere[0]) and y != len(matriceLumiere)):
                    if(str([(newPos), vecteur]) not in dicoDejaFait):
                        newABouger.append([(newPos), vecteur])
                        dicoDejaFait[str([(newPos), vecteur])] = 1
                    matriceLumiere[y][x] = "#"
            else:
                for d in direction[pos][vecteur]:
                    x=pt[0]+d[0]
                    y=pt[1]+d[1]
                    newPos = (x,y)
                    if(-1 not in newPos and x != len(matriceLumiere[0]) and y != len(matriceLumiere)):
                        if(str([(newPos), d]) not in dicoDejaFait):
                            newABouger.append([(newPos), d])
                            dicoDejaFait[str([(newPos), d])] = 1
                        matriceLumiere[y][x] = "#"
        ABouger = []
        ABouger = newABouger
    return compter(matriceLumiere)

score = []

for i in range(len(matrice2)):
    ABouger = [[(0,i), (1,0)]] 
    score.append(explorer(ABouger))

for i in range(len(matrice2)):
    ABouger = [[(len(matrice2[0])-1,i), (-1,0)]] 
    score.append(explorer(ABouger))

for i in range(len(matrice2[0])):
    ABouger = [[(i,0), (0,1)]] 
    score.append(explorer(ABouger))

for i in range(len(matrice2[0])):
    ABouger = [[(i,len(matrice2)-1), (0,-1)]] 
    score.append(explorer(ABouger))

print(max(score))


