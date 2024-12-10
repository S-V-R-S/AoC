
import time
start_time = time.time()

directions = [[0 , -1], [0, 1], (1, 0), (-1, 0)]

liste0 = []
with open('adventOfCode/2024/input10.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            letter = int(letter)
            if letter == 0:
                liste0.append((j,i))
            matrice[i].append(letter)

score = 0

for point in liste0:
    dico = {}
    dico[0] = set()
    dico[0].add(point)

    for i in range(1,10):
        dico[i] = set()
        for j in dico[i-1]:
            x,y = j[0], j[1]
            for dir in directions:
                x1 = x + dir[0]
                y1 = y + dir[1]
                if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice):
                    if matrice[y1][x1] == i:
                        dico[i].add((x1, y1))




    score += len(dico[9])

  


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", score)
