import re

def creer_tab():
        with open('adventOfCode/2024/input.txt', encoding="UTF-8", mode= "r") as file:  
                lignes = file.read().splitlines()
        return lignes


lignes = creer_tab()

somme = 0

propre = True
for ligne in lignes:
    dico = {}
    
    matches = re.finditer("mul\(\d+,\d+\)", ligne)
    for match in matches:
         dico[match.start()] = match.group()

    for i in range(len(ligne)):
         if ligne[i:i+7] == "don't()":
              propre = False
         if ligne[i:i+4] == "do()":
              propre = True
         if propre : 
              if i in dico:
                  x,y = re.findall("\d+", dico[i])
                  somme += int(x)*int(y)
     

print(somme)
        
