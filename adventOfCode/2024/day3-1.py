import re

                  
def creer_tab():
        with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
                lignes = file.read().splitlines()
        return lignes


lignes = creer_tab()
print(len(lignes))

somme = 0
for ligne in lignes:
     
    instructions = re.findall("mul\(\d+,\d+\)", ligne)
    for ins in instructions:
        x,y = re.findall("\d+", ins)
        somme += int(x)*int(y)
     
print(somme)