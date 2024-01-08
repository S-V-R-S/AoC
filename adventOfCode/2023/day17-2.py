import heapq
import time
start_time = time.time()
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

matrice = constructionMatrice(lectureDuFichier("adventOfCode\\2023\\input17.txt"))

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

heapq.heapify(avisiter)

while avisiter:

    pt = heapq.heappop(avisiter)

    dis, x, y, dx, dy, nbr = pt

    if y == len(matrice)-1 and x == len(matrice[0])-1 and nbr >= 4:
            print(dis)
            break
    
    if (x, y, dx, dy, nbr) not in visites:   

        visites.add((x,y,dx,dy,nbr))

        for dirx, diry in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dx == dirx and dy == diry and nbr < 10:
                nx = x + dirx
                ny = y + diry

                if nx >= 0 and nx <= len(matrice)-1 and ny>=0 and ny<= len(matrice)-1:
                    heapq.heappush(avisiter, (dis+matrice[ny][nx],nx, ny, dirx, diry, nbr+1))

            if nbr >= 4 or (dx,dy) == (0,0):
                if (dx != dirx or dy != diry) and ( dirx != -dx or diry != -dy):
                    nx = x + dirx
                    ny = y + diry

                    if nx >= 0 and nx <= len(matrice)-1 and ny>=0 and ny<= len(matrice)-1:
                        heapq.heappush(avisiter, (dis+matrice[ny][nx],nx, ny, dirx, diry, 1))


end_time = time.time()
execution_time = end_time - start_time

print(f"Le programme a mis {execution_time} secondes pour s'exécuter.")