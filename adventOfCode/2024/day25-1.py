import re
import math
from heapq import heappush, heappop
from enum import Enum
from functools import cache


with open('adventOfCode/2024/input25.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

groupes = []
groupe_courant = []
cerrures = []
cles = []
for ligne in lignes:
    if ligne.strip(): 
        groupe_courant.append(ligne) 
    else:
        if groupe_courant:  # Si un groupe courant existe, on le termine
            groupes.append(groupe_courant)
            groupe_courant = []
groupes.append(groupe_courant)

def score_cerrures(cerrure):
    score = []
    for i in range(5):
        s = 0
        for j in range(7):
            if cerrure[j][i] == "#":
                s += 1
        score.append(s)
    return score

def verifier(s1, s2):
    for i in range(len(s1)):
        if s1[i] + s2[i] > 7:
            return False
    return True

def score_cles(cerrure):
    score = []
    for i in range(5):
        s = 0
        for j in range(7):
            if cerrure[j][i] == ".":
                s += 1
        score.append(s)
    return score
        
for g in groupes:
    matrice = []
    for i, ligne in enumerate(g):
        matrice.append([])
        for j, letter in enumerate(ligne):
            matrice[i].append(letter)
    if matrice[0] == ['.', '.', '.', '.', '.']:
        cles.append(matrice)
    else:
        cerrures.append(matrice)
        

# for c in cerrures:
#     print(score_cerrures(c))
somme = 0
for c in cerrures:
    for cle in cles:
        if verifier(score_cerrures(c), score_cerrures(cle)):
            somme += 1
            
print(somme)

