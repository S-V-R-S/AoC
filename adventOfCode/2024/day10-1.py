
import time
start_time = time.time()

directions = [[0 , -1], [0, 1], (1, 0), (-1, 0)]

# je fais la matrice et recupere les positions des 0 
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

# pour tous les 0 trouves 
for point in liste0:
    dico = {}
    # pour la partie2 faut mettre une liste a la place du set 
    dico[0] = set()
    dico[0].add(point)
    #  les cles du dico c'est les nombres de 0 à 9
    # les valeurs c'est les positions qui sont atteignables  par les chemins

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
