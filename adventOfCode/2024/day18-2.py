
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

def creer_matrice(n):
    matrice = []
    for i in range(n+1):
        matrice.append([])
        for j in range(n+1):
            matrice[i].append(".")
    return matrice

def nodes_in(coor, matrice):
      nodes = []
      for dir in Direction:
        x = coor[0] + dir.value[0]
        y = coor[1] + dir.value[1]
        if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and matrice[y][x] != "#":
             nodes.append((x,y))
      return(nodes)

def dijkstra(matrice, point_A, point_B):
    path = []
    to_explore = [point_A]
    explored = []
    dico = {}
    dico[point_A] = 0

    while to_explore:
        node = to_explore[0]
        del to_explore[0]
        explored.append(node)
        curr_distance = dico[node]
        neighbours = nodes_in(node, matrice)
        for n in neighbours:
             if n not in explored and n not in to_explore:
                  to_explore.append(n)
                  dico[n] = curr_distance + 1

             elif dico[n] > curr_distance + 1:
                  dico[n] = curr_distance + 1

    if point_B in dico:
        return True
    else: return False

matrice = creer_matrice(70)
octets = []
with open('adventOfCode/2024/input18.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
for ligne in lignes:
    x,y = map(int, re.findall(r"-?\d+", ligne))
    octet = (x,y)
    octets.append(octet)

start = (0,0)
end = (70,70)

step = 2500
for o in octets[:step]:
    x, y = o
    matrice[y][x] = "#"

step -= 1
while dijkstra(matrice, start, end):
    step += 1
    print(step)
    x, y = octets[step]
    matrice[y][x] = "#"


print(octets[step])

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
