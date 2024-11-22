import re

def lire(nom: str):

    with open(nom, encoding="UTF-8", mode= "r") as file:  
            lignes = file.readlines()
    return lignes



# recuperation ligne
ligne = lire('adventOfCode/2022/input.txt')[0]
print(ligne)

for i in range(13,len(ligne) +1):
    chaine = ligne[i-13:i+1]
    if len(chaine) == len(set(chaine)):
     print(i+1)
     break