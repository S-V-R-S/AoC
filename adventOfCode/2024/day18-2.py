
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
    to_explore = [point_A]
    explored = []

    while to_explore:
        node = to_explore[0]
        del to_explore[0]
        explored.append(node)
        neighbours = nodes_in(node, matrice)
        for n in neighbours:
             if n == point_B: return True
             if n not in explored and n not in to_explore:
                  to_explore.append(n)
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

start_step = 1024
final_step = len(octets)

def test(s):
    matrice = creer_matrice(70)
    for o in octets[:s]:
        x, y = o
        matrice[y][x] = "#"
    return dijkstra(matrice, start, end)

while start_step != final_step - 1:
    step = start_step + (final_step - start_step) //2
    result = test(step)
    if result:
        start_step = step
    else:
        final_step = step
        

print(octets[start_step])
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
# (58, 62)
# 2989