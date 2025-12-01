
import time
start_time = time.time()

import re
import os

def creer_matrice():
    with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()
        matrice = []
        for i, ligne in enumerate(lignes):
            matrice.append([])
            for j, letter in enumerate(ligne):
                matrice[i].append(letter)
    return matrice

# a, b = int(re.findall("\d+", ligne)[0]), int(re.findall("\d+", ligne)[1])
with open('adventOfCode/2025/input1.txt', encoding="UTF-8", mode= "r") as file:  
# with open('adventOfCode/2025/test.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.read().splitlines()


max = 99
compteur = 0
pointeur = 50 


for ligne in lignes:
    lettre = ligne[0]
    nbr = int(ligne[1:])
     
    if lettre == "L":
        while nbr > pointeur:
            nbr = nbr - pointeur - 1
            if pointeur != 0:
                 compteur += 1
            pointeur = 99
        pointeur = pointeur - nbr
        if pointeur == 0:
            compteur += 1  
    else : 
        while nbr + pointeur > 99:
              nbr = nbr - (99 - pointeur + 1) 
              pointeur = 0
              compteur +=1
        pointeur = pointeur + nbr
    print(pointeur, compteur)

print(compteur)
        
        
                


























end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
