
import time
import re
import math
from heapq import heappush, heappop
from enum import Enum
start_time = time.time()

class Direction(Enum):
    NORD = (0 , -1)
    SUD = (0, 1)
    EST = (1, 0)
    OUEST = (-1, 0)

def dijkstra(matrice, start, end):

    to_explore = [start]
    explored = []
    dico = {}
    dico[start] = [0, None]
    scoreB = []

    while to_explore:
        node = to_explore[0]
        del to_explore[0]
        explored.append(node)

        neighbours = []
        for dir in Direction:
            x = node[0] + dir.value[0]
            y = node[1] + dir.value[1]

            if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and matrice[y][x] != "#":
                    neighbours.append((x,y))

        for new in neighbours:
            point = new
            total_cost = 1 + dico[node][0]

            if point == end:
                    scoreB.append(total_cost)
        
            if point in dico:
                if dico[point][0] > total_cost:
                    dico[point] = [total_cost, node]
                    if (point) not in to_explore:
                        to_explore.append(point)
            else:
                dico[point] = [total_cost, node]
                if point not in to_explore:
                    to_explore.append(point)

    path = []
    point = end
    while point != start:
         path.append(dico[point][1])
         point = dico[point][1]
    
    return path

def d(start, end):
    x,y = start
    x1, y1 = end
    distance = abs(x-x1) + abs(y-y1)
    
    return distance


with open('adventOfCode/2024/input20.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            if letter == "S":
                start = (j,i)
            if letter == "E":
                end = (j,i)
            matrice[i].append(letter)

path = dijkstra(matrice, start, end)
without = len(path)
print("sans tricher", without)
path.insert(0, end)
path.reverse()
somme = 0
print(without)
temps = 20
dico = {}
goal = 100
for i, point in enumerate(path):
    for j, destination in enumerate(path[i+goal:]):

        raccourci = d(point, destination)
        if raccourci <= temps:
            benef = j+goal - raccourci

            if benef >= goal:
                somme += 1



# 1037936
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", somme)
