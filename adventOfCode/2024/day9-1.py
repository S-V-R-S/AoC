
import time
start_time = time.time()

import re

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()


print(len(lignes))
lignes = lignes[0]

# 2333133121414131402
print(lignes)

# first step 
# 00...111...2...333.44.5555.6666.777.888899
first_step = []
full = True
index = 0
nbr = []

for i in lignes:
    if full:
        for j in range(int(i)):
            first_step.append(index)
            nbr.append(index)
        index += 1
    else:
         for j in range(int(i)):
            first_step.append(".")

    full = not(full)


print(first_step)
# 0099811188827773336446555566..............
second_step = []
index = len(nbr) - 1

for i in range(len(nbr)):
    if not(str(first_step[i]).isdigit()):
        second_step.append(nbr[index])
        index = index -1
    else:
        second_step.append(first_step[i])

print(second_step)


somme = 0
for i, number in enumerate(second_step):

    somme += int(number) * i

print(somme)
end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est")
