
import time
start_time = time.time()

import re

with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
    lignes = file.read().splitlines()


lignes = lignes[0]

# 2333133121414131402

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



reverse_list = first_step.copy()
reverse_list.reverse()
current_number = reverse_list[0]
add = 1
position = 0

for i in range(1, len(first_step)):
    if reverse_list[i] == ".": continue

    if reverse_list[i] == current_number:
        add += 1
    else:
        counter = 0
        for j in range(len(first_step)):
            if first_step[j] == current_number:
                break
            if first_step[j] == ".":
                counter += 1
            else: counter = 0
            if counter == add:
                for k in range(add):
                    first_step[-1 -position -k ] = "."
                    first_step[j-add+1+k] = current_number
                    
                break



        current_number = reverse_list[i]
        add = 1
        position = i

    if i == len(first_step) - 1:
        print("add", current_number, add)


somme = 0
sete = set()
for i, number in enumerate(first_step):
    if number != ".":
        somme += int(number) * i


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Le programme a dure {elapsed_time_ms:.2f} ms est la reponse est", somme)
# 6321896265143