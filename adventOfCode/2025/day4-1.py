
import time
start_time = time.time()

def creer_matrice():
    with open('adventOfCode/2025/input.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()
        matrice = []
        for i, ligne in enumerate(lignes):
            matrice.append([])
            for j, letter in enumerate(ligne):
                matrice[i].append(letter)
    return matrice

matrice = creer_matrice()

total = 0
for i, ligne in enumerate(matrice):
    for j, point in enumerate(ligne):
        compteur = 0
        if point != "@":
            continue
        for k in range(-1,2):
            for m in range(-1,2):
                x = i + k
                y = j + m
                if not(k == 0 and m ==0) and x>=0 and y >= 0 and x<len(matrice) and y<len(ligne):
                    if matrice[x][y] == "@" or matrice[x][y] =="x":
                        compteur +=1
                        
        if compteur < 4:
            total += 1
            matrice[i][j] = "x"
            
print(total)

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
