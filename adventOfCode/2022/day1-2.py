import os

def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:   
            lignes = file.readlines()
    return lignes

threeMaxCalories = [0,0,0]
currentCalories = 0

for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        currentCalories += int(ligne)
    else:
        if currentCalories > min(threeMaxCalories):
            threeMaxCalories[threeMaxCalories.index(min(threeMaxCalories))] = currentCalories
        currentCalories = 0

print(sum(threeMaxCalories))
