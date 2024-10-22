def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes

maxCalories = 0
currentCalories = 0

for ligne in lire('adventOfCode/2022/input.txt'):
    if(ligne.strip() != ""):
        currentCalories += int(ligne)
    else:
        if currentCalories > maxCalories:
            maxCalories = currentCalories
        currentCalories = 0

print(maxCalories)
