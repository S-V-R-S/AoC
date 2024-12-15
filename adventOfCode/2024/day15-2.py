
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

def pousser_terminator(matrice, move, x,y):
    m = matrice.copy()
    position = []
    check = 0
    if move == (0, 1):
        if matrice[y+1][x] == "[":
            position.append([x, x+1])
        else:
            position.append([x, x-1])

        etage = y + 2
        

        while etage < len(matrice):
            nbr_pt = 0
            p_t = []
            for x in position[check]:
                if matrice[etage][x] == "#":
                    return matrice, False
                if matrice[etage][x] == "[":
                    p_t.append(x+1)
                    p_t.append(x)
                if matrice[etage][x] == "]":
                    p_t.append(x-1)
                    p_t.append(x)
                if matrice[etage][x] == ".":
                    nbr_pt += 1
   
            if nbr_pt == len(position[check]):
                for i in range(len(position)):
                    for x in position[-1-i]:
                        if m[y + len(position)-i][x] in ['[', ']']:
                            m[y + 1 + len(position)-i][x] = m[y + len(position)-i][x]
                            m[y + len(position)-i][x] = "."
                return m, True
               
            etage += 1
            position.append(list(set(p_t)))
            check += 1


    if move == (0, -1):
        if matrice[y-1][x] == "[":
            position.append([x, x+1])
        else:
            position.append([x, x-1])

        etage = y - 2

        while etage < len(matrice):
            nbr_pt = 0
            p_t = []
            for x in position[check]:
                if matrice[etage][x] == "#":
                    return matrice, False
                if matrice[etage][x] == "[":
                    p_t.append(x+1)
                    p_t.append(x)
                if matrice[etage][x] == "]":
                    p_t.append(x-1)
                    p_t.append(x)
                if matrice[etage][x] == ".":
                    nbr_pt += 1
            
            if nbr_pt == len(position[check]):
                for i in range(len(position)):
                    for x in position[len(position)-1-i]:
                        if m[y - len(position)+i][x] in ['[', ']']:
                            m[y - 1 - len(position)+i][x] = m[y - len(position)+i][x]
                            m[y - len(position)+i][x] = "."
                        
                return m, True

            position.append(list(set(p_t)))
            check += 1               
            etage -= 1
        
    return matrice, False


def pousser(ligne_):
    ligne = ligne_.copy()
    if "." not in ligne:
        return ligne, 0
    for i in range(len(ligne)):
        if ligne[i] == "#":
            return ligne, 0
        
        if ligne[i] == ".":
            del ligne[i]
            ligne.insert(0, '@')
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
                    if  letter == "O":
                        matrice[i].append("[")
                        matrice[i].append("]")
                    else:
                        matrice[i].append(letter)
                        matrice[i].append(letter)
                        if letter == "@":
                            matrice[i][-1] = "."
                            robot = (len(matrice[i])-2, i)
            
            else:
                mouvements += ligne

print(robot)
print(matrice[robot[1]][robot[0]])
for ligne in matrice:
    print(ligne)


for i in mouvements:
    # print(i)
    x,y = robot
    move = direction[i]
    x1 = x + move[0]
    y1 = y + move[1]
    
    if 0 <= x1 < len(matrice[0]) and 0 <= y1 < len(matrice) and matrice[y1][x1] != "#":
        if matrice[y1][x1] == ".":
            robot = (x1,y1)
            matrice[y1][x1] = "@"
            matrice[y][x] = "."
        else:
            if move == (0 , -1):
                matrice_temp, possible = pousser_terminator(matrice, move, x,y)
                if possible:
                    matrice = matrice_temp                    
                    matrice[y1][x1] = "@"
                    robot = (x1,y1)
                    matrice[y][x] = "."

            if move == (0 , 1):
                matrice_temp, possible = pousser_terminator(matrice, move, x,y)
                if possible:
                    matrice = matrice_temp
                    matrice[y1][x1] = "@"
                    robot = (x1,y1)
                    matrice[y][x] = "."

            if move == (1 , 0):
                ligne = []
                for j in range(x1, len(matrice[0]), 1):
                    ligne.append(matrice[y1][j])
                # print("droite",ligne)
                new_ligne, x0 = pousser(ligne)
                if ligne != new_ligne:
                    for k, r in enumerate(new_ligne):
                        matrice[y1][x1+k] = r
                    matrice[y][x] = "."
                    robot = (x1,y1)

            if move == (-1 , 0):
                ligne = []
                for j in range(x1, -1, -1):
                    ligne.append(matrice[y1][j])
                # print("gauche",ligne)
                new_ligne, x0 = pousser(ligne)
                if ligne != new_ligne:
                    for k, r in enumerate(new_ligne):
                        matrice[y1][x1-k] = r
                    matrice[y][x] = "."
                    robot = (x1,y1)
    # for ligne in matrice:
    #     print(ligne)
    # input()   

somme = 0
for ligne in matrice:
    print(ligne)
for y, ligne in enumerate(matrice):
    for x, pt in enumerate(ligne):
        if pt == "[":
            somme += x + 100*y

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", somme)
# 1543141