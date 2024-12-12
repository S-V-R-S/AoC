
import time
start_time = time.time()

directions = [[0 , -1], [0, 1], (1, 0), (-1, 0)]
parcelles = set()

with open('adventOfCode/2024/input12.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
            parcelles.add((j,i))

prix = 0
while len(parcelles) != 0:
    p = parcelles.pop()
    same = [p]
    to_explore = [p]

    while to_explore:
        point = to_explore.pop()
        x, y = point

        for dir in directions:
            x1 = x + dir[0]
            y1 = y + dir[1]
            if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice):
                if matrice[y1][x1] == matrice[y][x] and (x1,y1) not in same:
                    same.append((x1, y1))
                    to_explore.append((x1, y1))
                    parcelles.remove((x1,y1))
    
    print(same)
    perimetre = 0
    for parcelle in same:
        x,y = parcelle
        for dir in directions:
            x1 = x + dir[0]
            y1 = y + dir[1]
            if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice):
                if (x1,y1) not in same:
                    perimetre += 1
            else:
                perimetre += 1

    prix += perimetre * len(same)
    
                
                    



print(prix)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# 1494342