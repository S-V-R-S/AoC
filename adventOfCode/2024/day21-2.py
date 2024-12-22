
import time
from itertools import product
from enum import Enum
start_time = time.time()

class Direction(Enum):
    NORD = (0 , -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

cache = {}
with open('adventOfCode/2024/input21.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()

R3 = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"],
]

R0 = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]

p3 = {
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "A": (2, 3)
}

p0 = {
    "^": (1, 0),
    "<": (0, 1),
    ">": (2, 1),
    "v": (1, 1),
    "A": (2, 0)
}

trad = {
   (-1,0) : "<",
   (0,1) : "v",
   (1,0) : ">",
   (0,-1) : "^",
}

A3 = p3["A"]
A0 = p0["A"]


def goto1(s, e):
        path = []
        start = p3[s]
        x,y = start
        dest = p3[e]

        dx = dest[0] - start[0]
        dy = dest[1] - start[1]
        liste = ""

        if (x + dx, y) !=  (0 , 3):
            if dx > 0:
                liste += trad[(1,0)]*abs(dx)
            if dx < 0:
                liste += trad[(-1,0)]*abs(dx) 
            if dy < 0:
                liste += trad[(0,-1)]*abs(dy)     
            if dy > 0:
                liste += trad[(0,1)]*abs(dy)
            liste+="A"
        if liste != "":       
            path.append(liste)
            liste = ""

        if (x , y + dy) !=  (0 , 3):
            if dy < 0:
                liste += trad[(0,-1)]*abs(dy)     
            if dy > 0:
                liste += trad[(0,1)]*abs(dy)
            if dx > 0:
                liste += trad[(1,0)]*abs(dx)
            if dx < 0:
                liste += trad[(-1,0)]*abs(dx) 
            liste+="A"
            
        if liste != "":
            if liste not in path:      
                path.append(liste)

        return path

def goto2(s, e):
        path = []
        start = p0[s]
        x,y = start
        dest = p0[e]

        dx = dest[0] - start[0]
        dy = dest[1] - start[1]
        liste = ""

        if (x + dx, y) !=  (0 , 0):
            if dx > 0:
                liste += trad[(1,0)]*abs(dx)
            if dx < 0:
                liste += trad[(-1,0)]*abs(dx) 
            if dy < 0:
                liste += trad[(0,-1)]*abs(dy)     
            if dy > 0:
                liste += trad[(0,1)]*abs(dy)
            liste+="A"
        if liste != "":       
            path.append(liste)
            liste = ""

        if (x , y + dy) !=  (0 , 0):
            if dy < 0:
                liste += trad[(0,-1)]*abs(dy)     
            if dy > 0:
                liste += trad[(0,1)]*abs(dy)
            if dx > 0:
                liste += trad[(1,0)]*abs(dx)
            if dx < 0:
                liste += trad[(-1,0)]*abs(dx) 
            liste+="A"
            
        if liste != "":
            if liste not in path:      
                path.append(liste)

        return path


def generation_combinations(dico):
    values = [dico[key] for key in sorted(dico.keys())]
    return [''.join(comb) for comb in product(*values)]


def trad1(code):
    start = "A"
    dico = {}
    for i, c in enumerate(code):
        dico[i] = goto1(start, c)
        start = c
    return generation_combinations(dico)


def recursivite(sequence, remaining):
    if (sequence,remaining) in cache:
        return cache[(sequence,remaining)] 
    
    sequence = "A" + sequence

    if remaining == 1:
        score = 0
        for p in range(len(sequence)-1):
            score += min(len(seq) for seq in goto2(sequence[p], sequence[p+1])) 

        cache[(sequence,remaining)] = score
        return score
    
    
    score = 0
    for p in range(len(sequence)-1):
        rep = []
        
        new = goto2(sequence[p], sequence[p+1])
        
        for i in new:
            rep.append(recursivite(i, remaining-1))

        score += min(rep) 

    cache[(sequence[1:],remaining)] = score
    return score   




somme = 0

for code in lignes:
    step1 = trad1(code)    
    rep1 = []
    print(step1)
    for s in step1:
        rep1.append(recursivite(s, 25))
    somme += min(rep1)*int(code[:3])


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", somme)
# 231309103124520
