
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


def cheated_couple(coor, matrice, cheated_list):

      for dir in Direction:
        x = coor[0] + dir.value[0]
        y = coor[1] + dir.value[1]
        if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]):
             cheated_list.append([coor, (x,y)])
      return cheated_list



def nodes_in(coor, matrice, magic):
      nodes = []
      for dir in Direction:
        x = coor[0] + dir.value[0]
        y = coor[1] + dir.value[1]
        if 0 <= x < len(matrice) and 0 <= y < len(matrice[0]) and (matrice[y][x] != "#" or (x,y) in magic):
             nodes.append((x,y))
      return(nodes)

def dijkstra(matrice, point_A, point_B, magic):
    if magic == [(10,7), (11,7)]:
        print(magic)
    to_explore = [point_A]
    explored = []
    dico = {}
    dico[point_A] = 0

    while to_explore:
        node = to_explore[0]
        del to_explore[0]
        explored.append(node)
        curr_distance = dico[node]
        neighbours = nodes_in(node, matrice, magic)
        for n in neighbours:
             if n not in explored and n not in to_explore:
                  to_explore.append(n)
                  dico[n] = curr_distance + 1

             elif dico[n] > curr_distance + 1:
                  dico[n] = curr_distance + 1

    return dico[point_B]

walls = []

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()
    matrice = []
    for i, ligne in enumerate(lignes):
        matrice.append([])
        for j, letter in enumerate(ligne):
            if letter == "S":
                start = (j,i)
            if letter == "E":
                end = (j,i)
            if letter == "#":
                walls.append((j, i))
            matrice[i].append(letter)

without = dijkstra(matrice, start, end, (-3,-3))
print("sans tricher", without)

cheated_list = []
for wall in walls:
     cheated_list = cheated_couple(wall, matrice, cheated_list)

score = {}
for triche in cheated_list:

        new = dijkstra(matrice, start, end, triche)
        if without-new not in score:
            score[without-new] = set()
        
        score[without-new].add((triche[0], triche[1]))


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
