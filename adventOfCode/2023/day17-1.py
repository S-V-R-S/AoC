def lectureDuFichier(chemin):
    f = open(chemin,"r")
    lignes = f.read()
    f.close()
    return lignes

def constructionMatrice(lignes):
    lignes = lignes.split("\n")
    matrice = []
    for i,l in enumerate(lignes):
        matrice.append([])
        for case in l.strip():
            matrice[i].append(int(case))
    return matrice

matrice = constructionMatrice(lectureDuFichier("advent code 2023\\test.txt"))

def leMoinsLoin():
    lml = None
    distance = float('inf')
    for p in avisiter:
        if p[0]<distance:
            distance = p[0]
            lml = p
    return lml 

# distance, x, y, directionx, directiony, nombre dans la direction
depart = (0,0,0,0,0,0)
visites = set()
avisiter = [depart]

print("exo1:")
while avisiter:

    pt = leMoinsLoin()

    avisiter.remove(pt)

    dis, x, y, dx, dy, nbr = pt

    if y == len(matrice)-1 and x == len(matrice[0])-1:
            print(dis)
            break
    
    if (x, y, dx, dy, nbr) not in visites:   

        visites.add((x,y,dx,dy,nbr))

        for dirx, diry in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dx == dirx and dy == diry and nbr < 3:
                nx = x + dirx
                ny = y + diry
                nbr += 1

                if nx >= 0 and nx <= len(matrice)-1 and ny>=0 and ny<= len(matrice)-1:
                    avisiter.append(((dis+matrice[ny][nx],nx, ny, dirx, diry, nbr)))


            if (dx != dirx or dy != diry) and ( dirx != -dx or diry != -dy):
                nx = x + dirx
                ny = y + diry

                if nx >= 0 and nx <= len(matrice)-1 and ny>=0 and ny<= len(matrice)-1:
                    avisiter.append(((dis+matrice[ny][nx],nx, ny, dirx, diry, 1)))



