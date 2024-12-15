
import re
import math
from heapq import heappush, heappop
from enum import Enum

import time
start_time = time.time()
    # x, y = list(map(int, re.findall(r"-?\d+", position)))


direction = {
    "^" : (0 , -1),
    "v" : (0, 1),
    ">" : (1, 0),
    "<" : (-1, 0)
}

def pousser(ligne_):
    ligne = ligne_.copy()
    if "." not in ligne:
        return ligne, 0
    for i in range(len(ligne)):
        if ligne[i] == "#":
            return ligne, 0
        if ligne[i] == ".":
            ligne[i] = "0"
            ligne[0] = "."
            return ligne, i

with open('adventOfCode/2024/input15.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    mouvements = ""

    for i, ligne in enumerate(lignes):
        if ligne != "":
            if ligne[0] in ["#","@", ".", "O"]:
                matrice.append([])
                for j, letter in enumerate(ligne):
                    matrice[i].append(letter)
                    if letter == "@":
                        robot = (j,i)
            
            else:
                mouvements += ligne

nb = 0
for y, ligne in enumerate(matrice):
    for x, pt in enumerate(ligne):
        if pt == "O":
            nb += 1


for i in mouvements:
    # print(i)
    x,y = robot
    move = direction[i]
    x1 = x + move[0]
    y1 = y +move[1]
    
    if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice) and matrice[y1][x1] != "#":
        if matrice[y1][x1] == ".":
            robot = (x1,y1)
            matrice[y1][x1] = "@"
            matrice[y][x] = "."
        else:
            if move == (0 , -1):
                ligne = []
                for j in range(y1, -1, -1):
                    ligne.append(matrice[j][x1])
                # print("monte",ligne)
                new_ligne, y0 = pousser(ligne)
                if ligne != new_ligne:
                    matrice[-y0+y1][x1] = "O"
                    matrice[y1][x1] = "@"
                    matrice[y][x] = "."
                    robot = (x1,y1)

            if move == (0 , 1):
                ligne = []
                for j in range(y1, len(matrice), 1):
                    ligne.append(matrice[j][x1])
                # print("descend",ligne)
                new_ligne, y0 = pousser(ligne)
                if ligne != new_ligne:
                    matrice[y0+y1][x1] = "O"
                    matrice[y1][x1] = "@"
                    matrice[y][x] = "."
                    robot = (x1,y1)

            if move == (1 , 0):
                ligne = []
                for j in range(x1, len(matrice[0]), 1):
                    ligne.append(matrice[y1][j])
                # print("droite",ligne)
                new_ligne, x0 = pousser(ligne)
                if ligne != new_ligne:
                    matrice[y1][x1+x0] = "O"
                    matrice[y1][x1] = "@"
                    matrice[y][x] = "."
                    robot = (x1,y1)

            if move == (-1 , 0):
                ligne = []
                for j in range(x1, -1, -1):
                    ligne.append(matrice[y1][j])
                # print("gauche",ligne)
                new_ligne, x0 = pousser(ligne)
                if ligne != new_ligne:
                    matrice[y1][x1-x0] = "O"
                    matrice[y1][x1] = "@"
                    matrice[y][x] = "."
                    robot = (x1,y1)



somme = 0

for y, ligne in enumerate(matrice):
    for x, pt in enumerate(ligne):
        if pt == "O":
            somme += x + 100*y


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", somme)
# 1505963