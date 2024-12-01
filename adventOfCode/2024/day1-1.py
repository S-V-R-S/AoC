import re
import os

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
        lignes = file.readlines()

list_a = []
list_b = []
for ligne in lignes:
    a, b = int(re.findall("\d+", ligne)[0]), int(re.findall("\d+", ligne)[1])
    list_a.append(a)
    list_b.append(b)


list_b.sort()
list_a.sort()

total_distance = 0
for i in range(0, len(list_b)):
      total_distance += abs(list_a[i] - list_b[i])

